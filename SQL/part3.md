# 🔗 SQL JOIN – বিস্তারিত ব্যাখ্যা (বাংলায়)

## ❓ কেন ব্যবহার করা হয় `JOIN`?
`JOIN` ব্যবহার করা হয় **একাধিক টেবিলকে যুক্ত করে ডেটা দেখানোর জন্য**।  
যেহেতু রিলেশনাল ডেটাবেজে ডেটা আলাদা টেবিলে থাকে, তাই সম্পর্কিত টেবিলগুলোর মধ্যে ডেটা একত্রে দেখাতে `JOIN` ব্যবহার করা হয়।

---

## 🔤 JOIN-দের প্রকারভেদ ও কাজ

| JOIN টাইপ | কাজ | কী রিটার্ন করে |
|-----------|------|----------------|
| `INNER JOIN` | মিল পাওয়া রেকর্ডগুলো | উভয় টেবিলে ম্যাচ থাকা রেকর্ড |
| `LEFT JOIN` | বাম টেবিলের সব, আর মিল থাকলে ডান টেবিল | না মিললেও বাম দিকটা থাকবে |
| `RIGHT JOIN` | ডান টেবিলের সব, আর মিল থাকলে বাম টেবিল | না মিললেও ডান দিকটা থাকবে |
| `FULL JOIN` | উভয় টেবিলের সব রেকর্ড | মিল থাকুক বা না থাকুক |

---

## 🔤 মৌলিক সিনট্যাক্স:

### 🔹 INNER JOIN
```sql
SELECT A.column1, B.column2
FROM TableA A
INNER JOIN TableB B
ON A.common_field = B.common_field;
```

### 🔹 LEFT JOIN
```sql
SELECT A.column1, B.column2
FROM TableA A
LEFT JOIN TableB B
ON A.common_field = B.common_field;
```

### 🔹 RIGHT JOIN
```sql
SELECT A.column1, B.column2
FROM TableA A
RIGHT JOIN TableB B
ON A.common_field = B.common_field;
```

### 🔹 FULL JOIN *(সব ডেটাবেজ সাপোর্ট করে না)*  
```sql
SELECT A.column1, B.column2
FROM TableA A
FULL OUTER JOIN TableB B
ON A.common_field = B.common_field;
```

---

## 🧠 বাস্তব উদাহরণ

### 🛒 উদাহরণ: `customers` এবং `orders` টেবিল

#### 🔹 ১. যেসব কাস্টমারের অর্ডার আছে (INNER JOIN):
```sql
SELECT customers.name, orders.order_date
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id;
```

#### 🔹 ২. সব কাস্টমার দেখাও, অর্ডার থাকুক বা না থাকুক (LEFT JOIN):
```sql
SELECT customers.name, orders.order_date
FROM customers
LEFT JOIN orders
ON customers.customer_id = orders.customer_id;
```

#### 🔹 ৩. সব অর্ডার দেখাও, কাস্টমার না থাকলেও (RIGHT JOIN):
```sql
SELECT customers.name, orders.order_date
FROM customers
RIGHT JOIN orders
ON customers.customer_id = orders.customer_id;
```

---

## 📌 সহজে মনে রাখার টিপস

### ✅ মনে রাখার নিয়ম:
> **"JOIN মানে — ডেটাবেসের সম্পর্ক জোড়া লাগাও!"**

- `INNER` → শুধু যেটা দুই টেবিলে মিলে  
- `LEFT` → বাম দিকের সব, ডান দিক মিলে গেলে  
- `RIGHT` → ডান দিকের সব, বাম দিক মিলে গেলে  
- `FULL` → দুই দিকেই থাকুক বা না থাকুক — সবই!

---

## 🔐 অতিরিক্ত টিপ:
* টেবিলের Alias (`A`, `B` ইত্যাদি) ব্যবহার করলে কোড পড়তে সহজ হয়।
* `JOIN`-এর সাথে `WHERE`, `GROUP BY`, `ORDER BY` সব ব্যবহার করা যায়।

---

```sql
SELECT C.name, COUNT(O.order_id) AS total_orders
FROM customers C
LEFT JOIN orders O
ON C.customer_id = O.customer_id
GROUP BY C.name;
```

> এতে প্রতিটি কাস্টমারের মোট অর্ডারের সংখ্যা দেখাবে, এমনকি যাদের অর্ডারই নেই!

