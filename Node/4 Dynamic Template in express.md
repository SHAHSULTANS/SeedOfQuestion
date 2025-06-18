---
# 🚀 Working with Dynamic Content & Adding Template Engines in Express
---

## 🤔 প্রশ্ন:

> Express দিয়ে কিভাবে আমরা dynamic content সার্ভ করবো?
>
> কিভাবে template engine যুক্ত করে আমরা ডেটা সহ HTML render করতে পারি?

---

## 🧠 Dynamic Content মানে কী?

Dynamic content মানে হচ্ছে **server-side থেকে ডেটা এনে সেটা HTML-এর মধ্যে বসিয়ে রেন্ডার করা**।
এই কাজটায় সাহায্য করে **Template Engines**।

> ‍💬 উদাহরণ: User details, blog post, product list — এসব static HTML দিয়ে handle করা যায় না, তাই dynamic rendering লাগে।

---

## 🧰 Common Template Engines in Express:

| Engine         | File Extension | Syntax Style          | Use Case                         |
| -------------- | -------------- | --------------------- | -------------------------------- |
| **EJS**        | `.ejs`         | HTML + JS tags        | সহজ ও পরিচিত, সব কাজে ভাল        |
| **Pug**        | `.pug`         | Indented Syntax       | কম্প্যাক্ট UI, Rapid prototyping |
| **Handlebars** | `.hbs`         | Mustache-style `{{}}` | Clean templates, CMS-style apps  |

---

## 🧪 উদাহরণ: আমরা EJS ব্যবহার করবো

---

### 📁 Folder Structure:

```
project/
├── views/
│   ├── home.ejs
│   ├── about.ejs
│   └── users.ejs
├── public/
│   └── style.css
└── server.js
```

---

### ✅ Step 1: Install express এবং ejs

```bash
npm init -y
npm install express ejs
```

---

### ✅ Step 2: server.js (ES6 module style)

```js
import express from "express";
import path from "path";
import { fileURLToPath } from "url";

const app = express();
const PORT = 3000;

// 📍 For __dirname in ES6
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// 📍 Set view engine to EJS
app.set("view engine", "ejs");

// 📍 Static folder serve
app.use(express.static(path.join(__dirname, "public")));

// 📍 Routes
app.get("/", (req, res) => {
  res.render("home", { username: "Shanto", title: "Home Page" });
});

app.get("/about", (req, res) => {
  res.render("about", { pageTitle: "About Us" });
});

app.get("/users", (req, res) => {
  const users = [
    { name: "Alice", email: "alice@example.com" },
    { name: "Bob", email: "bob@example.com" },
    { name: "Charlie", email: "charlie@example.com" },
  ];
  res.render("users", { users });
});

app.listen(PORT, () => {
  console.log(`🚀 Server is running at http://localhost:${PORT}`);
});
```

---

### ✅ Step 3: views/home.ejs

```html
<!DOCTYPE html>
<html>
  <head>
    <title><%= title %></title>
    <link rel="stylesheet" href="/style.css" />
  </head>
  <body>
    <h1>Hello <%= username %> 👋</h1>
    <p>Welcome to Express with EJS</p>
  </body>
</html>
```

---

### ✅ Step 4: views/about.ejs

```html
<h2><%= pageTitle %></h2>
<p>This site is powered by Express and EJS!</p>
```

---

### ✅ Step 5: views/users.ejs

```html
<h2>User List</h2>
<ul>
  <% users.forEach(user => { %>
  <li><strong><%= user.name %></strong> - <%= user.email %></li>
  <% }) %>
</ul>
```

---

## 🔍 Template Syntax Breakdown:

| Syntax            | Description                          |
| ----------------- | ------------------------------------ |
| `<%= variable %>` | Output HTML-encoded (safe) value     |
| `<%- variable %>` | Output raw HTML                      |
| `<% JS logic %>`  | Run JavaScript (e.g., loop, if/else) |
| `<% include %>`   | Include another template (partials)  |

---

## 🌍 রিয়েল লাইফ ব্যবহার:

| বাস্তব প্রয়োগ             | কীভাবে ব্যবহার হয়                           |
| ------------------------- | ------------------------------------------- |
| Blog Page                 | Post title, body, author dynamically দেখানো |
| Admin Panel               | User list, orders table দেখানো              |
| Invoice Generator         | Template এ ডেটা বসিয়ে PDF তৈরি              |
| Feedback / Contact Page   | Success message বা error message দেখানো     |
| Ecommerce Product Listing | Cart, Wishlist ডেটা সহ পেজ দেখানো           |

---

## 💡 Bonus: Template Partials ব্যবহার (reuse layout)

#### 👉 layout/header.ejs

```html
<header>
  <h1>My App</h1>
</header>
```

#### 👉 views/home.ejs

```html
<%- include("layout/header") %>
<h2>Welcome <%= username %></h2>
```

---

## ✅ Static Asset Serve করো:

```js
app.use(express.static(path.join(__dirname, "public")));
```

> CSS, images, JS files — সব `public` ফোল্ডার থেকে serve হবে।

---

## 📌 সহজে মনে রাখার টিপস

> **Dynamic Content = Template Engine + Express Route + Data Passing**
>
> 🔹 `app.set("view engine", "ejs")`
> 🔹 `res.render("page", { title, data })`
> 🔹 HTML-এ `<%= value %>` দিয়ে inject করো
> 🔹 Dynamic UI বানাও loop ও logic দিয়ে
> 🔹 Static asset `public/` ফোল্ডারে রাখো

---
