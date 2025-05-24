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

# 🔢 SQL BETWEEN – বিস্তারিত ব্যাখ্যা (বাংলায়)

## ❓ কেন ব্যবহার করা হয় `BETWEEN`?
`BETWEEN` অপারেটর ব্যবহার করা হয় **দুটি নির্দিষ্ট মানের মধ্যে থাকা রেকর্ড** খুঁজে বের করার জন্য।  
এটি **inclusive**, অর্থাৎ শুরু এবং শেষ মানও রেজাল্টে অন্তর্ভুক্ত থাকে।

---

## 🔤 মৌলিক সিনট্যাক্স:
```sql
SELECT column1, column2
FROM table_name
WHERE column_name BETWEEN value1 AND value2;
```

- `value1` = lower bound (নিম্ন মান)
- `value2` = upper bound (উচ্চ মান)

---

## 🧠 বাস্তব উদাহরণ:

### 🔹 ১. মার্কস ৫০ থেকে ৮০ এর মধ্যে যাদের আছে:
```sql
SELECT name, marks
FROM students
WHERE marks BETWEEN 50 AND 80;
```
> যেসব ছাত্রের মার্কস ৫০ থেকে ৮০ এর মধ্যে, তারা রেজাল্টে আসবে।

---

### 🔹 ২. জন্ম তারিখ ২০০০ থেকে ২০০5 এর মধ্যে:
```sql
SELECT name, birth_date
FROM users
WHERE birth_date BETWEEN '2000-01-01' AND '2005-12-31';
```
> ২০০০ থেকে ২০০৫ সালের মধ্যে জন্ম নেয়া ইউজারদের তথ্য দেখাবে।

---

### 🔹 ৩. বেতন ৩০,০০০ থেকে ৫০,০০০ এর মধ্যে:
```sql
SELECT name, salary
FROM employees
WHERE salary BETWEEN 30000 AND 50000;
```
> ৩০ থেকে ৫০ হাজার টাকার মধ্যে যাদের বেতন, তাদের দেখাবে।

---

## 📌 সহজে মনে রাখার টিপস

### ✅ মনে রাখার নিয়ম:
> **"BETWEEN মানে — মাঝের জিনিসগুলা ধর ভাই!"**  
> শুরু আর শেষ দুইটাও ধরা হবে!

- `BETWEEN 10 AND 20` → ১০, ১১, ..., ২০ পর্যন্ত সব অন্তর্ভুক্ত  
- ডেট, নাম্বার, এমনকি টেক্সটেও `BETWEEN` কাজ করে (Alphabetical range)

---

## 🔐 অতিরিক্ত টিপ:
* `BETWEEN` এর বিকল্প:  
  ```sql
  column >= value1 AND column <= value2
  ```
  কিন্তু `BETWEEN` লেখা আরও পরিষ্কার ও সংক্ষিপ্ত।

* NOT BETWEEN ও আছে:  
  ```sql
  WHERE age NOT BETWEEN 18 AND 30;
  ```


# ✅ SQL IN – বিস্তারিত ব্যাখ্যা (বাংলায়)

## ❓ কেন ব্যবহার করা হয় `IN`?
`IN` অপারেটর ব্যবহার করা হয় যখন আমরা চাই **একটি কলাম কোনো একটি নির্দিষ্ট মানের তালিকার মধ্যে আছে কি না তা যাচাই করতে**।  
এটি অনেকগুলো `OR` কন্ডিশন লিখার বদলে সহজে সমাধান করে।

---

## 🔤 মৌলিক সিনট্যাক্স:
```sql
SELECT column1, column2
FROM table_name
WHERE column_name IN (value1, value2, value3, ...);
```

- একাধিক মান চেক করতে `IN` ব্যবহার করা হয়
- প্রতিটি মান কমা দিয়ে আলাদা করতে হয়

---

## 🧠 বাস্তব উদাহরণ:

### 🔹 ১. নির্দিষ্ট কয়েকজন ছাত্রের তথ্য বের করা:
```sql
SELECT name, marks
FROM students
WHERE name IN ('Rahim', 'Karim', 'Jannat');
```
> শুধু Rahim, Karim, Jannat এর তথ্য দেখাবে।

---

### 🔹 ২. নির্দিষ্ট কিছু বিভাগে থাকা কর্মচারীদের তালিকা:
```sql
SELECT name, department
FROM employees
WHERE department IN ('HR', 'IT', 'Finance');
```
> HR, IT, ও Finance বিভাগের কর্মচারীরা রেজাল্টে থাকবে।

---

### 🔹 ৩. `NOT IN` ব্যবহার:
```sql
SELECT name
FROM customers
WHERE city NOT IN ('Dhaka', 'Chittagong');
```
> শুধু Dhaka এবং Chittagong ছাড়া অন্য শহরের কাস্টমার দেখাবে।

---

## 📌 সহজে মনে রাখার টিপস

### ✅ মনে রাখার নিয়ম:
> **"IN মানে — এই লিস্টের ভিতরে থাকলেই দে!"**  
> মান গুলো যেন একটা `shopping list` এর মতো!

- `IN ('a', 'b', 'c')` → যদি ‘a’ বা ‘b’ বা ‘c’ হয়, তবে রেজাল্টে রাখো  
- `NOT IN (...)` → ঐগুলা বাদ দিয়ে বাকি সব রাখো

---

## 🔐 অতিরিক্ত টিপ:
* `IN` কাজ করে **subquery** এর সাথেও:
```sql
SELECT name
FROM employees
WHERE id IN (SELECT employee_id FROM project_members);
```
> যারা কোনো প্রজেক্টে কাজ করছে তাদের নাম দেখাবে।

* `IN` অপারেটর case-sensitive হতে পারে, ডাটাবেসের উপর নির্ভর করে।



# 🔍 SQL LIKE – বিস্তারিত ব্যাখ্যা (বাংলায়)

## ❓ কেন ব্যবহার করা হয় `LIKE`?
`LIKE` অপারেটর ব্যবহার করা হয় **টেক্সট ডেটা থেকে প্যাটার্ন অনুযায়ী মিল খুঁজে বের করতে**।  
যখন আমরা চাই নাম, ইমেইল, শহরের নাম ইত্যাদি **আংশিক মেলানো**, তখন `LIKE` খুব কার্যকর।

---

## 🔤 মৌলিক সিনট্যাক্স:
```sql
SELECT column1, column2
FROM table_name
WHERE column_name LIKE 'pattern';
```

- `%` → ০ বা তার বেশি কোনো অক্ষর
- `_` → যেকোনো একটি অক্ষর

---

## 🧠 বাস্তব উদাহরণ:

### 🔹 ১. যেসব নাম "A" দিয়ে শুরু:
```sql
SELECT name
FROM students
WHERE name LIKE 'A%';
```
> যেমন: "Ahsan", "Amina", "Akash"

---

### 🔹 ২. যেসব নাম "n" দিয়ে শেষ:
```sql
SELECT name
FROM students
WHERE name LIKE '%n';
```
> যেমন: "Rehan", "Tuhin", "Hasan"

---

### 🔹 ৩. যেসব নামের মধ্যে "mi" আছে:
```sql
SELECT name
FROM students
WHERE name LIKE '%mi%';
```
> যেমন: "Amina", "Tamim", "Samira"

---

### 🔹 ৪. দ্বিতীয় অক্ষর যদি 'a' হয়:
```sql
SELECT name
FROM students
WHERE name LIKE '_a%';
```
> যেমন: "Rafi", "Tania", "Halim"

---

## 📌 সহজে মনে রাখার টিপস

### ✅ মনে রাখার নিয়ম:
> **"LIKE মানে — এমন কিছু খুঁজে দে, যেটার সাথে মিল আছে!"**  
> `%` মানে অনেক কিছু — `_` মানে একটি!

- `LIKE 'A%'` → A দিয়ে শুরু  
- `LIKE '%n'` → n দিয়ে শেষ  
- `LIKE '%mi%'` → মাঝে "mi" আছে

---

## 🔐 অতিরিক্ত টিপ:
* `LIKE` case-sensitive হতে পারে (MySQL-এ নয়, কিন্তু PostgreSQL বা Oracle-এ হতে পারে)
* অনেক ডেটাবেজে `ILIKE` (case-insensitive LIKE) ও আছে
* `NOT LIKE` দিয়ে বিপরীত মান খোঁজা যায়:
```sql
WHERE name NOT LIKE 'R%';
```

