# 🏷️ SQL AS – বিস্তারিত ব্যাখ্যা (বাংলায়)

## ❓ কেন ব্যবহার করা হয় `AS`?
`AS` ব্যবহার করা হয় **কলাম বা টেবিলের জন্য একটি অস্থায়ী নাম (Alias)** দিতে।  
এটি মূলত ফলাফলকে আরো **বোঝার সহজ এবং সুন্দর** করে তোলে।

---

## 🔤 মৌলিক সিনট্যাক্স:

### 🔹 কলামের জন্য:
```sql
SELECT column_name AS alias_name
FROM table_name;
```

### 🔹 টেবিলের জন্য:
```sql
SELECT A.column_name, B.column_name
FROM table_name1 AS A
JOIN table_name2 AS B
ON A.id = B.id;
```

> `AS` ঐচ্ছিক; শুধু `alias_name` লিখলেও চলে।

---

## 🧠 বাস্তব উদাহরণ

### 🔹 ১. কলামের জন্য সুন্দর নাম:
```sql
SELECT name AS customer_name, age AS customer_age
FROM customers;
```
> ফলাফলে কলামের নাম হবে: `customer_name` ও `customer_age`

---

### 🔹 ২. গণনার পর Alias:
```sql
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department;
```

---

### 🔹 ৩. টেবিলের জন্য Alias:
```sql
SELECT C.name, O.order_date
FROM customers AS C
JOIN orders AS O
ON C.customer_id = O.customer_id;
```
> `C` এবং `O` হলো টেবিলের সংক্ষিপ্ত নাম, কোড কমপ্যাক্ট রাখে।

---

## 📌 সহজে মনে রাখার টিপস

### ✅ মনে রাখার নিয়ম:
> **"AS মানে — এই নামে দেখাও!"**

- `name AS full_name` → “name” কলামকে `full_name` নামে দেখাও
- `AVG(salary) AS avg_salary` → গড় বেতনকে `avg_salary` নামে দেখাও
- `table_name AS T` → টেবিলকে `T` নামে ডাকে

---

## 🔐 অতিরিক্ত টিপ:
* `AS` মূলত **presentation purposes**-এর জন্য।  
* এটি ডেটা পরিবর্তন করে না, শুধু **রেজাল্টে নাম পরিবর্তন** করে দেখায়।
* অনেক সময় SQL ভিউ বা সাবকোয়েরিতে `AS` খুবই দরকার হয়।

```sql
SELECT name, salary * 0.1 AS bonus
FROM employees;
```

> এখানে `bonus` হলো হিসাব করা মানের নতুন নাম।




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

