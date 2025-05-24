# 🐚 SQL in a Nutshell

**SQL (Structured Query Language)** is a standard programming language used to manage and manipulate **relational databases**.

## 🔧 Core Functions
- **SELECT** – retrieve data
- **INSERT** – add new data
- **UPDATE** – modify existing data
- **DELETE** – remove data
- **CREATE** – create tables/databases 
- **DROP** – delete tables/databases

## 📦 Used With
Relational Database Management Systems (RDBMS) like:
- MySQL
- PostgreSQL
- SQLite
- Microsoft SQL Server
- Oracle

## 🧠 Example Query
```sql
SELECT name, age FROM users WHERE age > 18;
```

# 🧠 Is SQL Only for Relational Databases?

**Yes, mostly.** SQL is designed for **relational databases**, but:

- Some **non-relational systems** offer **SQL-like interfaces**
- These are for **ease of use** and **familiarity**, not strict relational behavior

➡️ **Bottom line:** SQL = Relational by design, but flexible in modern ecosystems.
# 📘 SQL SELECT – Basic Syntax with Description

The **SELECT** statement is used to **retrieve information from a database** by specifying the columns and table from which the data should be fetched.

## 🔤 Syntax
```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition
GROUP BY column
HAVING condition
ORDER BY column ASC|DESC
LIMIT number;
```
# Clause and Keyword
- **Keywords** are individual reserved words in SQL like `SELECT`, `FROM`, `WHERE`, `JOIN`, etc.
- A **Clause** is a **combination of a keyword plus additional elements** that together perform a specific function in a query.

For example:
- `SELECT column1, column2` → the **SELECT clause** (keyword `SELECT` + list of columns)
- `WHERE age > 18` → the **WHERE clause** (keyword `WHERE` + condition)

So, a **clause** is a meaningful unit of SQL syntax composed of a keyword and its associated expressions, whereas a **keyword** is just the reserved word itself.

> **In short:**  
> A *clause* is a part of a SQL statement defined by a keyword *and* its parameters or expressions.

# 🗂️ What is a Database Schema?

A **database schema** is the **blueprint or structure** that defines how data is organized in a database.

## 📦 It Includes:
- Tables and their columns
- Data types (e.g., INT, VARCHAR)
- Relationships between tables (e.g., foreign keys)
- Indexes
- Constraints (e.g., NOT NULL, UNIQUE)
- Views, triggers, stored procedures (in some cases)

## 🧠 Think of it like:
> A **schema** is to a database what a **plan** is to a building.  
> It defines how everything is arranged and how it all connects.

## 📝 Example
```sql
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(100),
  age INT,
  class_id INT,
  FOREIGN KEY (class_id) REFERENCES classes(id)
);
```

# 🌟 SQL `DISTINCT` – In a Nutshell

## ❓ Why Use `DISTINCT`?
The `DISTINCT` keyword is used to **remove duplicate rows** from the result set.  
It ensures that the returned data contains **only unique combinations** of the selected columns.

## 🔤 Basic Syntax
```sql
SELECT DISTINCT column1, column2, ...
FROM table_name;
```

# 🔢 SQL COUNT – In a Nutshell

## ❓ Why Use `COUNT`?
The `COUNT` function is used to **count the number of rows** that match a specified condition in a table.

## 🔤 Basic Syntax
```sql
SELECT COUNT(*) FROM table_name;

SELECT COUNT(*) FROM customers;
-- Counts total rows in the 'customers' table

SELECT COUNT(email) FROM customers;
-- Counts only rows where 'email' is NOT NULL
```

# 🔢 COUNT with DISTINCT in SQL

## ❓ Purpose:
To **count the number of unique (distinct) values** in a specific column.

## 🔤 Syntax:
```sql
SELECT COUNT(DISTINCT column_name)
FROM table_name;
```

# 🎯 SQL SELECT WHERE – In a Nutshell

## ❓ Why Use `WHERE`?
The `WHERE` clause is used to **filter records** in a SQL query.  
It tells the database to **only return rows that meet a specific condition**.

Without `WHERE`, SQL returns **all rows** from the table.

---

## 🔤 Basic Syntax:
```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;

SELECT name, department
FROM employees
WHERE department = 'HR';#use single quotes
```
# 🔍 SQL WHERE Clause with Multiple Conditions

## 📌 Purpose:
Use `AND`, `OR`, `BETWEEN`, `IN`, and `LIKE` with `WHERE` to **create more precise filters**.

---

## 🔤 Syntax:
```sql
SELECT column1, column2
FROM table_name
WHERE condition1 AND|OR condition2;
```
# 🎯 চ্যালেঞ্জ নাম্বার ১

## 📌 প্রশ্ন (বাংলায়):
একজন গ্রাহক আমাদের দোকানে তার মানিব্যাগ ফেলে গেছেন! তাকে জানাতে আমাদের তার ইমেইল ঠিকানাটি খুঁজে বের করতে হবে।  
**গ্রাহকের নাম: Nancy Thomas**  
➤ আমরা কীভাবে তার ইমেইলটি খুঁজে বের করব?

---

## 🧾 উত্তর (SQL):

```sql
SELECT email
FROM customers
WHERE first_name = 'Nancy' AND last_name = 'Thomas';
```

# ❓ Why Use Single Quotes `' '` in SQL, Not Double Quotes `" "`?

## 🔤 Rule in SQL:
- ✅ **Single quotes `' '`** are used to **represent string literals**  
  Example:
  ```sql
  SELECT * FROM users WHERE name = 'Alice';
  ```

*🔒 Double quotes " " are used to represent identifiers (like column or table names), especially when*

Example:
  ```sql
  SELECT "first Name" FROM "user Data";
  ```

# 📊 SQL ORDER BY – বিস্তারিত ব্যাখ্যা (বাংলায়)

## ❓ কেন ব্যবহার করা হয় `ORDER BY`?
`ORDER BY` ক্লজ ব্যবহার করা হয় **ডেটাকে সাজিয়ে দেখানোর জন্য**।  
এটি রেজাল্টসেটকে একটি নির্দিষ্ট কলামের ভিত্তিতে **ascending (ASC)** বা **descending (DESC)** ক্রমে সাজায়।

---

## 🔤 মৌলিক সিনট্যাক্স:
```sql
SELECT column1, column2
FROM table_name
ORDER BY column1 [ASC|DESC];
```

* `ASC` = ঊর্ধ্বক্রমে সাজানো (Ascending) — (default)
* `DESC` = অবরোহ ক্রমে সাজানো (Descending)

---

## 🧠 বাস্তব উদাহরণ:

### 🔹 ১. ছাত্রদের নাম অক্ষর ক্রমে সাজানো:
```sql
SELECT name, marks
FROM students
ORDER BY name ASC;
```
> অক্ষর অনুযায়ী নাম সাজিয়ে দেখাবে (A to Z)।

---

### 🔹 ২. সর্বোচ্চ মার্কস অনুসারে সাজানো:
```sql
SELECT name, marks
FROM students
ORDER BY marks DESC;
```
> সর্বোচ্চ মার্কসধারী ছাত্র প্রথমে দেখাবে।

---

### 🔹 ৩. একাধিক কলাম অনুসারে সাজানো:
```sql
SELECT name, department, age
FROM employees
ORDER BY department ASC, age DESC;
```
> প্রথমে ডিপার্টমেন্ট অনুযায়ী সাজাবে,  
> তারপর একই ডিপার্টমেন্টের মধ্যে বয়স অনুসারে সাজাবে।

---

## 📌 সহজে মনে রাখার টিপস

### ✅ মনে রাখার নিয়ম:
> **"ORDER BY মানে — সাজিয়ে দে ভাই!"**  
> যেভাবে বলবো, ঠিক সেভাবেই রেজাল্ট সাজিয়ে দে!

* `ORDER BY name ASC` → নাম অক্ষর অনুযায়ী সাজাও  
* `ORDER BY salary DESC` → বেশি salary আগে দেখাও

---

## 🔐 অতিরিক্ত টিপ:
* `ORDER BY` সবসময় `SELECT`-এর শেষে আসে।  
* অন্য ক্লজ যেমন `WHERE`, `GROUP BY` থাকলেও `ORDER BY` সবার শেষে!


# 📉 SQL LIMIT – বিস্তারিত ব্যাখ্যা (বাংলায়)

## ❓ কেন ব্যবহার করা হয় `LIMIT`?
`LIMIT` ক্লজ ব্যবহার করা হয় **রেজাল্টসেট থেকে নির্দিষ্ট সংখ্যক সারি (row)** দেখানোর জন্য।  
যখন আমরা শুধু **কয়েকটি রেকর্ড দেখতে চাই**, তখন `LIMIT` ব্যবহার করি।

---

## 🔤 মৌলিক সিনট্যাক্স:
```sql
SELECT column1, column2
FROM table_name
LIMIT number;
```

- `number` = কতগুলো রেকর্ড তুমি দেখতে চাও

---

## 🧠 বাস্তব উদাহরণ:

### 🔹 ১. প্রথম ৫ জন ছাত্রের তথ্য দেখানো:
```sql
SELECT name, marks
FROM students
LIMIT 5;
```
> শুধুমাত্র প্রথম ৫টি রেকর্ড দেখাবে।

---

### 🔹 ২. সর্বোচ্চ মার্কসধারী প্রথম ৩ জন:
```sql
SELECT name, marks
FROM students
ORDER BY marks DESC
LIMIT 3;
```
> সর্বোচ্চ মার্কস অনুসারে সাজিয়ে প্রথম ৩ জন ছাত্র দেখাবে।

---

### 🔹 ৩. পেজিনেশন/স্কিপ করার জন্য OFFSET সহ ব্যবহার:
```sql
SELECT name
FROM customers
LIMIT 5 OFFSET 10;
```
> প্রথম ১০টি রেকর্ড স্কিপ করে পরবর্তী ৫টি রেকর্ড দেখাবে (যেমন পেজ 3)।

---

## 📌 সহজে মনে রাখার টিপস

### ✅ মনে রাখার নিয়ম:
> **"LIMIT মানে — ভাই, কষ্ট করে বেশি দিস না, অল্প দে!"**  
> যতটুকু দরকার, ততটুকু রেকর্ড দেখাও।

- `LIMIT 10` → প্রথম ১০টি রেকর্ড দাও  
- `LIMIT 3 OFFSET 6` → ৬টা স্কিপ করে পরের ৩টা দাও

---

## 🔐 অতিরিক্ত টিপ:
* `LIMIT` সাধারণত `ORDER BY` এর পরে ব্যবহার করা হয়
* সব ডাটাবেসে `LIMIT` কাজ নাও করতে পারে (যেমন SQL Server-এ `TOP` বা `FETCH` ব্যবহার হয়)

