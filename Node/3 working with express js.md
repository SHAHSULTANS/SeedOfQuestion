# 🧭 Express JS Router: পথঘাট আলাদা করে গোছানোর নিয়ম

## 🤔 প্রশ্ন:

> Express Router দিয়ে কী হয়? এটা কবে, কেন, কিভাবে ব্যবহার করবো?

Express Router ব্যবহার করে আমরা বড় অ্যাপকে ছোট ছোট রুট ফাইলে ভাগ করে রাখতে পারি — maintain করা সহজ হয়, গুছানো থাকে।

---

## 📦 ধরো — তুমি বানাচ্ছো একটা Blog App

ফোল্ডার স্ট্রাকচার:

```
blog-app/
├── routes/
│   ├── posts.js
│   └── users.js
├── server.js
└── package.json
```

---

## ✅ Step 1: server.js – Router ফাইল ইনপোর্ট করা

```js
import express from "express";
import postsRouter from "./routes/posts.js";
import usersRouter from "./routes/users.js";

const app = express();
const PORT = 3000;

// Middleware
app.use(express.json());

// Router attach করা
app.use("/posts", postsRouter);
app.use("/users", usersRouter);

app.listen(PORT, () => {
  console.log(`🚀 Server is running at http://localhost:${PORT}`);
});
```

---

## ✅ Step 2: routes/posts.js – Router বানানো

```js
import express from "express";
const router = express.Router();

// GET all posts
router.get("/", (req, res) => {
  res.send("📄 All blog posts");
});

// GET single post
router.get("/:id", (req, res) => {
  res.send(`📄 Post ID: ${req.params.id}`);
});

export default router;
```

---

## ✅ Step 3: routes/users.js – অন্য একটা Router

```js
import express from "express";
const router = express.Router();

// GET all users
router.get("/", (req, res) => {
  res.send("👥 All users");
});

// GET user by ID
router.get("/:id", (req, res) => {
  res.send(`👤 User ID: ${req.params.id}`);
});

export default router;
```

---

## 🔍 ব্যাখ্যা:

| বিষয়               | কাজ                                                 |
| ------------------ | --------------------------------------------------- |
| `express.Router()` | ছোট ছোট রাউট বানানোর জন্য                           |
| `app.use()`        | মূল অ্যাপের সাথে আলাদা রাউট ফাইল যুক্ত করার জন্য    |
| Modular Routing    | ভিন্ন ফাইলে রাউট রাখলে কোড পড়তে ও maintain করতে সহজ |
| `req.params`       | URL path থেকে dynamic অংশ (যেমন \:id) পাওয়ার জন্য   |

---

## 🌍 রিয়েল ওয়ার্ল্ড ব্যবহার

| Context              | Router ব্যবহার কোথায় হয়?                   |
| -------------------- | ------------------------------------------ |
| Large Web App        | রাউট ভাগ করে – auth, blog, product ইত্যাদি |
| API Development      | প্রতিটি resource এর জন্য আলাদা router      |
| Admin + Public Panel | আলাদা router handle করতে সুবিধা            |

---

## 💡 Bonus: Middleware শুধু একটা Router এর জন্য

```js
router.use((req, res, next) => {
  console.log("✅ Post route accessed");
  next();
});
```

---

## 📌 সহজে মনে রাখার টিপস

> "বড় অ্যাপকে ছোট করে ভাঙো — `Router` দিয়ে route আলাদা করো"
> `express.Router()` → আলাদা ফাইলে route → `app.use()` দিয়ে attach করো

---

# 📁 Express + ES6 Modules এ Static File Serve করার সঠিক উপায়

## 🤔 প্রশ্ন:

> আমরা যদি ES6 module ব্যবহার করি (`type: "module"`), তখন কি `express.static()` ভিন্নভাবে handle করতে হয়?

একদম ঠিক! ES6 module ব্যবহারে কিছু পার্থক্য আসে।

---

## ✅ Setup: ES6 module চালু করো

**package.json** এ এটা যোগ করো:

```json
{
  "type": "module"
}
```

---

## ✅ ফোল্ডার স্ট্রাকচার:

```
project/
├── public/
│   ├── index.html
│   └── style.css
└── server.js
```

---

## ✅ Step 1: server.js – Static serve করা (ES6 way)

```js
import express from "express";
import path from "path";
import { fileURLToPath } from "url";

const app = express();
const PORT = 3000;

// ✅ ES6 এ __dirname তৈরি করো
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// ✅ public ফোল্ডার serve করো
app.use(express.static(path.join(__dirname, "public")));

app.listen(PORT, () => {
  console.log(`🚀 Server is running at http://localhost:${PORT}`);
});
```

---

## 🔍 ব্যাখ্যা:

| বিষয়              | ES6 modules এর behavior          |
| ----------------- | -------------------------------- |
| `__dirname`       | ES6-এ নেই, তাই নিজে বানাতে হয়    |
| `fileURLToPath()` | current module path বের করে      |
| `path.join()`     | platform-independent static path |

---

## 🌍 রিয়েল ওয়ার্ল্ড ব্যবহার

| Context              | Static File                      |
| -------------------- | -------------------------------- |
| React/Vue SPA Deploy | Serve `build/` folder statically |
| Admin Dashboard      | Serve fonts, CSS, client JS      |
| Landing Page         | Serve index.html + styles/images |

---

## 💡 Bonus: Serve from custom path

```js
app.use("/static", express.static(path.join(__dirname, "public")));
```

Then visit →  
`http://localhost:3000/static/index.html`

---

## ✅ উদাহরণ index.html

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Static with ES6</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <h1>Hello Static ES6 🚀</h1>
  </body>
</html>
```

---

## 📌 সহজে মনে রাখার টিপস

> `import.meta.url → fileURLToPath → __dirname → express.static()`
