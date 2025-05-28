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

