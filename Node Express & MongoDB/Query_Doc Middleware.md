MongoDB ও Mongoose-এ **Query Middleware** এবং **Document Middleware**—এই দুইটা একেবারে ভিন্ন জিনিস, যদিও দুটোই middleware হিসেবেই কাজ করে।

---

## ✅ সংক্ষিপ্ত পার্থক্য:

| দিক                | Query Middleware                                                      | Document Middleware                                                  |
| ------------------ | --------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **কখন চলে?**       | যখন `.find()`, `.findOne()`, `.update()` এর মতো **query অপারেশন চলে** | যখন `.save()`, `.create()`, `.remove()` বা `.deleteOne()` হয়         |
| **কী modify করে?** | Query modify করে → কি ডেটা fetch হবে                                  | Document modify করে → কি ডেটা ডাটাবেজে যাবে বা ডাটাবেজ থেকে আসবে     |
| **উদ্দেশ্য**       | ডেটা fetch করার আগে/পরে extra filter, populate ইত্যাদি করা            | ডেটা সংরক্ষণের আগে validation, encryption, slug generate ইত্যাদি করা |
| **Access**         | `this` মানে হয় **query object**                                       | `this` মানে হয় **document object**                                   |

---

## 🧪 উদাহরণে ব্যাখ্যা

### 📌 1. Query Middleware

```js
// ✅ Query Middleware: Hide secret tours from any find query
tourSchema.pre(/^find/, function (next) {
  this.find({ secretTour: { $ne: true } }); // Query কে modify করা হচ্ছে
  next();
});
```

👉 যখনই `Tour.find()` বা `Tour.findOne()` চলবে, সেখানে `secretTour: true` ফিল্ড exclude করা হবে।

---

### 📌 2. Document Middleware

```js
// ✅ Document Middleware: Create slug before saving
tourSchema.pre("save", function (next) {
  this.slug = this.name.toLowerCase().split(" ").join("-");
  next();
});
```

👉 যখন নতুন ট্যুর তৈরি বা সংরক্ষণ করা হবে (e.g. `.save()` বা `.create()`), তখন `name` থেকে একটি slug তৈরি করে সেটি ফিল্ডে বসিয়ে দেবে।

---

## 💡 Real-world Example:

- **Query Middleware**:
  → আপনি একজন user only public data দেখতে পারেন। তাই `.find()`-এর আগে middleware দিয়ে private ডেটা exclude করেন।

- **Document Middleware**:
  → User password hash করে save করতে চান? তাহলে `.save()`-এর আগে password hash করবেন।

---

## 🧠 Middleware Hook টাইপ:

| Middleware টাইপ     | Hook নাম                                       |
| ------------------- | ---------------------------------------------- |
| Query Middleware    | `pre('find')`, `pre(/^find/)`, `post('find')`  |
| Document Middleware | `pre('save')`, `post('save')`, `pre('remove')` |

---

## 📌 সহজে মনে রাখার টিপস:

- 🔍 **Query Middleware** = যখন তুমি ডেটা _খুঁজো_
  👉 কাজ করে `.find()`, `.update()` এর আগে
  👉 Modify করে query (e.g. hide secret)

- 📄 **Document Middleware** = যখন তুমি ডেটা _তৈরি বা আপডেট_ করো
  👉 কাজ করে `.save()`, `.create()` এর আগে
  👉 Modify করে ডকুমেন্ট (e.g. password hash)

---

**`this` keyword টা Document Middleware, Query Middleware, এবং Aggregation Middleware-এ কী বোঝায়?** — এটা system-level context বোঝার জন্য **খুবই গুরুত্বপূর্ণ**।

নিচে প্রতিটা middleware context-এ `this` কী বোঝায়, বাস্তব উদাহরণসহ ব্যাখ্যা করলাম।

---

## 🧠 `this` এর ভিন্ন ব্যবহার – Middleware অনুযায়ী

| Middleware Type        | `this` কী বোঝায়                                |
| ---------------------- | ---------------------------------------------- |
| Document Middleware    | 👉 Mongoose Document (i.e. `doc`)              |
| Query Middleware       | 👉 Mongoose Query Object (`this.getQuery()`)   |
| Aggregation Middleware | 👉 Aggregation Object (i.e. `this.pipeline()`) |

---

## 🔹 1. Document Middleware – `this = document`

```js
tourSchema.pre("save", function (next) {
  console.log(this); // 👉 এই `this` হলো save হতে যাওয়া document

  this.slug = slugify(this.name, { lower: true }); // ✅ document এর ভেতরের ফিল্ডে কাজ
  next();
});
```

### ✅ এখানে `this` মানে:

- একটি Tour ডকুমেন্ট
- তুমি এটাতে `.name`, `.price`, `.save()` ইত্যাদি সব access করতে পারো

---

## 🔹 2. Query Middleware – `this = query object`

```js
tourSchema.pre(/^find/, function (next) {
  console.log(this.getQuery()); // 👉 এখানে this = mongoose query instance

  this.find({ secretTour: { $ne: true } }); // ✅ query modify করা হচ্ছে
  next();
});
```

### ✅ এখানে `this` মানে:

- একটি query instance
- তুমি `.find()`, `.select()`, `.getQuery()` এসব ব্যবহার করতে পারো

🎯 **ব্যবহার:**

- query থেকে `secretTour` বাদ দেওয়া
- timestamp log করা

---

## 🔹 3. Aggregation Middleware – `this = aggregation object`

```js
tourSchema.pre("aggregate", function (next) {
  console.log(this.pipeline()); // 👉 এখানে `this` = aggregation query object

  this.pipeline().unshift({ $match: { secretTour: { $ne: true } } });
  next();
});
```

### ✅ এখানে `this` মানে:

- একটি aggregation pipeline object
- তুমি `.pipeline()` দিয়ে current pipeline access করতে পারো

🎯 **ব্যবহার:**

- aggregation শুরু হবার আগে pipeline modify করা

---

## ⚖️ তুলনামূলক চিত্র:

| Context            | `this` কী বোঝায়?            | Access কী কী?                         |
| ------------------ | --------------------------- | ------------------------------------- |
| `pre("save")`      | Document (`Tour` doc)       | `.name`, `.price`, `.save()`          |
| `pre("find")`      | Query object                | `.getQuery()`, `.find()`, `.select()` |
| `pre("aggregate")` | Aggregation pipeline object | `.pipeline()`                         |

---

## 🧪 বাস্তব উদাহরণ (সব ৩টি একত্রে):

```js
// Document middleware
tourSchema.pre("save", function (next) {
  console.log("🧾 Document middleware - name:", this.name);
  next();
});

// Query middleware
tourSchema.pre(/^find/, function (next) {
  console.log("🔎 Query middleware - filters:", this.getQuery());
  next();
});

// Aggregation middleware
tourSchema.pre("aggregate", function (next) {
  console.log("📊 Aggregation middleware - pipeline:", this.pipeline());
  next();
});
```

---

## 📌 সহজে মনে রাখার টিপস:

| ধরন         | `this` কী?      | মনে রাখার ট্রিক                             |
| ----------- | --------------- | ------------------------------------------- |
| Document    | `Tour` document | ডাটা **save** করার আগে, `this = document`   |
| Query       | query object    | **find** এর আগে query টা চেক করার সুযোগ     |
| Aggregation | pipeline object | aggregate হলে, pipeline চেইন modify করা যায় |

---
