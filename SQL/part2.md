# 🧮 SQL Aggregate Functions – বিস্তারিত ব্যাখ্যা (বাংলায়)

## ❓ Aggregate Function কেন ব্যবহার করা হয়?
Aggregate Functions ব্যবহার করা হয় **একাধিক রেকর্ডের উপর গণনা চালিয়ে একটি মাত্র মান রিটার্ন করার জন্য**।  
যেমন: মোট কতজন, গড় কত, সর্বোচ্চ কত ইত্যাদি।

---

## 🧠 Aggregate Functions এর ধরন ও কাজ

| Function | কাজ | উদাহরণ |
|----------|------|---------|
| `COUNT()` | রেকর্ড সংখ্যা গুনে | মোট ছাত্র সংখ্যা |
| `SUM()` | মোট যোগফল বের করে | মোট সেলস |
| `AVG()` | গড় মান বের করে | গড় মার্কস |
| `MAX()` | সর্বোচ্চ মান | সর্বোচ্চ বেতন |
| `MIN()` | সর্বনিম্ন মান | সবচেয়ে কম দাম |

---

## 🔤 মৌলিক সিনট্যাক্স:
```sql
SELECT AGG_FUNC(column_name)
FROM table_name
[WHERE condition];
```

---

## 🔎 বাস্তব উদাহরণ:

### 🔹 ১. মোট ছাত্র সংখ্যা:
```sql
SELECT COUNT(*) FROM students;
```

---

### 🔹 ২. গড় মার্কস:
```sql
SELECT AVG(marks) FROM students;
```

---

### 🔹 ৩. সর্বোচ্চ বেতন:
```sql
SELECT MAX(salary) FROM employees;
```

---

### 🔹 ৪. কোন শহরে সবচেয়ে কম অর্ডার হয়েছে:
```sql
SELECT MIN(order_amount) FROM orders;
```

---

### 🔹 ৫. সেলস-এর মোট যোগফল:
```sql
SELECT SUM(sales_amount) FROM sales;
```

---

## 📌 সহজে মনে রাখার টিপস

### ✅ মনে রাখার নিয়ম:
> **"Aggregate মানে — একসাথে করে একটিই ফলাফল!"**

- `COUNT()` → কতটা আছে?  
- `SUM()` → মোট কত টাকা/মার্কস?  
- `AVG()` → গড় কত?  
- `MAX()` → সবচেয়ে বড় মান  
- `MIN()` → সবচেয়ে ছোট মান

---

## 🔐 অতিরিক্ত টিপ:
* Aggregate Function প্রায়ই `GROUP BY` এর সাথে ব্যবহার করা হয় (যেমন: ডিপার্টমেন্ট অনুযায়ী গড় বেতন)
* `NULL` মান সাধারণত গণনায় ধরেনা

```sql
SELECT department, AVG(salary)
FROM employees
GROUP BY department;
```

# 🧩 SQL GROUP BY – বিস্তারিত ব্যাখ্যা (বাংলায়)

## ❓ কেন ব্যবহার করা হয় `GROUP BY`?
`GROUP BY` ব্যবহার করা হয় **ডেটাকে কোনো একটি বা একাধিক কলামের ভিত্তিতে গ্রুপ (দল) করে ফেলতে**,  
তারপর সেই প্রতিটি গ্রুপের উপর **Aggregate Function** (যেমন `COUNT()`, `SUM()`, `AVG()` ইত্যাদি) প্রয়োগ করতে।

---

## 🔤 মৌলিক সিনট্যাক্স:
```sql
SELECT column_name, AGG_FUNC(another_column)
FROM table_name
GROUP BY column_name;
```

- `GROUP BY` সবসময় `WHERE` এর পরে এবং `ORDER BY` এর আগে আসে।
- `GROUP BY` এর সাথে সাধারণত Aggregate Functions ব্যবহার করা হয়।

---

## 🧠 বাস্তব উদাহরণ:

### 🔹 ১. প্রতিটি বিভাগের গড় বেতন:
```sql
SELECT department, AVG(salary)
FROM employees
GROUP BY department;
```
> প্রতিটি ডিপার্টমেন্ট অনুযায়ী গড় বেতন দেখাবে।

---

### 🔹 ২. প্রতিটি শহরের মোট কাস্টমার:
```sql
SELECT city, COUNT(*) as total_customers
FROM customers
GROUP BY city;
```
> প্রতিটি শহরে কতজন কাস্টমার আছে তা দেখাবে।

---

### 🔹 ৩. প্রতিটি প্রোডাক্টের মোট বিক্রি:
```sql
SELECT product_id, SUM(sales_amount)
FROM sales
GROUP BY product_id;
```

---

### 🔹 ৪. একাধিক কলাম দিয়ে গ্রুপিং:
```sql
SELECT department, gender, COUNT(*)
FROM employees
GROUP BY department, gender;
```
> প্রতিটি ডিপার্টমেন্টে নারী ও পুরুষ কর্মচারীর সংখ্যা আলাদা আলাদা দেখাবে।

---

## 📌 সহজে মনে রাখার টিপস

### ✅ মনে রাখার নিয়ম:
> **"GROUP BY মানে — ডেটাকে দলে দলে ভাগ করে, তারপর গোনা শুরু কর!"**

- `GROUP BY city` → শহর অনুযায়ী আলাদা করে  
- `GROUP BY department` → ডিপার্টমেন্ট অনুযায়ী ভাগ করো  
- প্রতিটি গ্রুপের উপর Aggregate Function চালানো যায়

---

## 🔐 অতিরিক্ত টিপ:
* `GROUP BY` ছাড়া `AVG()`, `COUNT()` এসব Aggregate Function পুরো টেবিলের উপর কাজ করে।
* যদি `GROUP BY` দাও, তাহলে **SELECT-এ থাকা অন্য কলামগুলো হয় `GROUP BY`-তে থাকতে হবে অথবা Aggregate Function-এ**।

```sql
-- ✅ Valid
SELECT department, MAX(salary)
FROM employees
GROUP BY department;

-- ❌ Invalid (name না GROUP BY-তে, না aggregate)
SELECT department, name
FROM employees
GROUP BY department;
```

# 🧾 SQL HAVING – বিস্তারিত ব্যাখ্যা (বাংলায়)

## ❓ কেন ব্যবহার করা হয় `HAVING`?
`HAVING` ক্লজ ব্যবহার করা হয় **`GROUP BY`-এর পর গ্রুপ করা ডেটার উপর শর্ত (condition) বসানোর জন্য**।  
যেখানে `WHERE` সাধারণ রো-গুলোর উপর কাজ করে, `HAVING` কাজ করে গ্রুপের উপর।

---

## 🔤 মৌলিক সিনট্যাক্স:
```sql
SELECT column_name, AGG_FUNC(column_name)
FROM table_name
GROUP BY column_name
HAVING AGG_FUNC(column_name) condition;
```

- `HAVING` সবসময় `GROUP BY`-এর পরে আসে।
- Aggregate Function এর উপর শর্ত বসাতে হলে `HAVING` ব্যবহার করতেই হবে।

---

## 🧠 বাস্তব উদাহরণ:

### 🔹 ১. যেসব বিভাগে গড় বেতন ৫০,০০০ এর বেশি:
```sql
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;
```

---

### 🔹 ২. যেসব শহরে ৫ জনের বেশি কাস্টমার:
```sql
SELECT city, COUNT(*) AS total_customers
FROM customers
GROUP BY city
HAVING COUNT(*) > 5;
```

---

### 🔹 ৩. যেসব প্রোডাক্টে মোট সেলস ১০,০০০ টাকার বেশি:
```sql
SELECT product_id, SUM(sales_amount) AS total_sales
FROM sales
GROUP BY product_id
HAVING SUM(sales_amount) > 10000;
```

---

## 📌 সহজে মনে রাখার টিপস

### ✅ মনে রাখার নিয়ম:
> **"WHERE — রো-গুলোর ফিল্টার।  
> GROUP BY — দলে ভাগ কর।  
> HAVING — দলে দলে শর্ত বসাও!"**

- `WHERE` → গ্রুপিংয়ের আগে ফিল্টার
- `HAVING` → গ্রুপিংয়ের পরে ফিল্টার

---

## 🔐 অতিরিক্ত টিপ:
* `HAVING` ছাড়া Aggregate Function এর উপর শর্ত বসানো যায় না
* চাইলে `HAVING`-এ alias ব্যবহার করা যায়:
```sql
SELECT city, COUNT(*) AS total_customers
FROM customers
GROUP BY city
HAVING total_customers > 5;
```

