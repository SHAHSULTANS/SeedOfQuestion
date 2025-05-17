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

