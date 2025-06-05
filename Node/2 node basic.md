## ⚙️ Node.js Core Modules – বাংলায় সহজ গাইড

---

### 📌 কী হলো Core Module?

Node.js-এর সাথে built-in ভাবে যেসব module আসে, যেগুলো **install না করেও** `require()` দিয়ে সরাসরি ব্যবহার করা যায় — সেগুলোই হলো **Core Modules**।

✅ এগুলো Performance ও Security-optimized, কারণ এগুলো C/C++ এবং JavaScript দিয়ে Node.js-এর ভেতরেই তৈরি।

---

### 🔰 কিছু গুরুত্বপূর্ণ Core Modules:

| Module   | কাজ                                         |
| -------- | ------------------------------------------- |
| `fs`     | File System – ফাইল পড়া/লেখা                |
| `path`   | Path handling – ডিরেক্টরি/ফাইল path ঠিক করা |
| `http`   | Server তৈরি করা                             |
| `os`     | Operating System সংক্রান্ত info             |
| `url`    | URL parsing                                 |
| `events` | Event-driven programming support            |
| `crypto` | Cryptographic functions (hash, encrypt)     |

---

## 🧪 উদাহরণসহ ব্যবহার

---

### 1️⃣ `fs` – File System Module

```js
const fs = require("fs");

// ✅ ফাইল পড়া (async)
fs.readFile("demo.txt", "utf-8", (err, data) => {
  if (err) return console.log("Error:", err);
  console.log(data);
});
```

---

### 2️⃣ `path` – Path Utility

```js
const path = require("path");

const filePath = path.join(__dirname, "folder", "file.txt");
console.log(filePath);
```

---

### 3️⃣ `http` – Basic Web Server

```js
const http = require("http");

const server = http.createServer((req, res) => {
  res.write("Hello from Node.js!");
  res.end();
});

server.listen(3000, () => {
  console.log("Server running at http://localhost:3000");
});
```

---

### 4️⃣ `os` – System Information

```js
const os = require("os");

console.log("OS Type:", os.type());
console.log("Total Memory:", os.totalmem());
```

---

### 5️⃣ `events` – Custom Event Handling

```js
const EventEmitter = require("events");

const myEmitter = new EventEmitter();

myEmitter.on("message", () => {
  console.log("Message event triggered!");
});

myEmitter.emit("message"); // ✅ Run event
```

---

### 📦 Core Module vs External Module

| বিষয়              | Core Module (e.g., fs, path) | External Module (e.g., express) |
| ----------------- | ---------------------------- | ------------------------------- |
| Install লাগে?     | না                           | হ্যাঁ (`npm install`)           |
| Built-in support? | হ্যাঁ                        | না                              |
| Performance       | দ্রুত                        | নির্ভর করে                      |

---

## 📌 সহজে মনে রাখার টিপস

> Node.js-এর সাথে built-in যেসব module আসে, সেগুলো হলো Core Modules  
> `require("module-name")` দিয়েই সরাসরি ব্যবহার করা যায় — install করতে হয় না  
> File system, server, path, OS info, event-driven কাজ — সব কিছুর জন্য ready-made solution আছে!

---

🔍 প্র্যাকটিস করার জন্য তুমি একটা mini CLI app বানাতে পারো, যেখানে `fs`, `path`, `os` এবং `events` একসাথে ব্যবহার করা হবে — চাইলে আমি সেটার template বানিয়ে দিতে পারি।

## 📡 `server.listen()` – কেন লাগে Node.js এ?

---

### 📌 সংজ্ঞা:

Node.js এ `server.listen()` ব্যবহার করা হয় **server-কে নির্দিষ্ট port-এ চালু করার জন্য**, যেন তা **incoming request** গ্রহণ করতে পারে।

👉 এটা না দিলে server তৈরি হলেও, **কোনো client connect করতে পারবে না** — কারণ সেটা **"শোনে না"**।

---

## 🧠 ব্যাখ্যা:

```js
const http = require("http");

const server = http.createServer(function (req, res) {
  res.end("Hello World");
});

server.listen(3000, () => {
  console.log("Server is running on port 3000");
});
```

---

### 🔍 কী করে `listen()`?

1. এটি বলে — "এই port (যেমন `3000`) এ আমি প্রস্তুত আছি"
2. Server এখন HTTP request পাবে
3. Callback (যেমন console.log) optional — শুধু জানায় server চালু হয়েছে কিনা

---

## ❓ `listen()` ছাড়া কি হবে?

```js
const server = http.createServer((req, res) => {
  res.end("Hi");
});

// ❌ কিন্তু এখানে listen() নেই
```

এই কোড চলবে ঠিকই, কিন্তু:

> 🔴 server **চালু হবে না**,  
> 🛑 **কোনো browser hit করলে response আসবে না**,  
> ⚠️ Node.js-এ কিছুই শোনার মত port bind হয়নি

---

## 🎯 Port কী?

**Port হলো একধরনের virtual door**, যেটা দিয়ে external client (যেমন browser বা mobile app) তোমার server-এর সাথে কথা বলে।

| Port Number    | সাধারণ ব্যবহৃত কাজ     |
| -------------- | ---------------------- |
| `80`           | HTTP (default)         |
| `443`          | HTTPS (secure)         |
| `3000`         | Development (commonly) |
| `5000`, `8080` | API servers            |

---

### 🛠️ Real-life Analogy:

> imagine তুমি একটা দোকান খুলেছো (server বানিয়েছো)  
> কিন্তু যদি তুমি দরজা না খোলো (listen না করো), কেউ ভেতরে ঢুকতে পারবে না।

---

## ✅ উপকারিতা:

| কাজ                                | `server.listen()` ছাড়া হয়? |
| ---------------------------------- | --------------------------- |
| Client থেকে request গ্রহণ করা      | ❌ না                       |
| Port খুলে server চালু করা          | ❌ না                       |
| Callback দিয়ে শুরু সফল কিনা জানানো | ✅ হ্যাঁ                    |

---

## 📌 সহজে মনে রাখার টিপস

> `createServer()` মানে দোকান বানানো  
> `listen()` মানে দোকান খোলা – port নাম্বার দিয়ে  
> না খুললে কেউ client হয়ে কিছু জানতে পারবে না!

```js
server.listen(3000, () => {
  console.log("Server is live at http://localhost:3000");
});
```

---

## 🧠 কেন লাগে Node.js server, যখন Physical server আছেই?

---

### 📌 সরাসরি উত্তর:

🔹 **Physical Server** হলো একটি বাস্তব বা virtual কম্পিউটার (যেমন AWS, DigitalOcean)  
🔹 **Node.js Server** হলো সেই কম্পিউটারে চলা **একটা প্রোগ্রাম**, যা HTTP request handle করে

> 👉 Node.js server না থাকলে, browser থেকে পাঠানো কোনো request কিভাবে process হবে — কে জানবে কী data দিতে হবে?

---

## 🖥️ একটি বাস্তব উদাহরণ:

ধরো, তুমি বানালে একটা ওয়েবসাইট — `myshop.com`

এখন কেউ সেই সাইটে গেলে কী হয়?

1. তার ব্রাউজার থেকে আসে HTTP request → `GET /home`
2. সেটি প্রথমে যায় একটি **physical server**-এ (যেখানে ওয়েবসাইট host করা আছে)
3. এরপর সেই সার্ভারে চলা **Node.js server প্রোগ্রাম** বুঝে নেয়, কী করতে হবে
4. তারপর ডেটাবেস দেখে, কিছু logic চালায়, এবং HTML/JSON/response পাঠিয়ে দেয়

---

## ⚙️ Component-wise Breakdown:

| Component       | ভূমিকা                                          |
| --------------- | ----------------------------------------------- |
| Physical Server | OS, File System, RAM, CPU — এটি একটা কম্পিউটার  |
| Node.js Program | HTTP request ধরার জন্য তৈরি করা JS অ্যাপ্লিকেশন |
| Browser         | Client — যেখান থেকে request আসে                 |

---

## 🧩 তাহলে Node.js Server এর দরকার কেন?

| কারণ                 | ব্যাখ্যা                                                        |
| -------------------- | --------------------------------------------------------------- |
| 📬 HTTP Request ধরতে | browser থেকে আসা GET, POST ইত্যাদি request কে বুঝে সাড়া দিতে    |
| 🔧 Custom logic      | ইউজারের request অনুযায়ী নিজের নিয়মে ডেটা পাঠানো বা গণনা করা যায় |
| 📡 REST API তৈরি     | মোবাইল বা ওয়েব অ্যাপে ব্যবহৃত backend বানানো যায়                |
| ⚡ Performance ভালো  | Node.js non-blocking nature এর জন্য দ্রুত response দেওয়া যায়    |
| 🧠 Maintainable      | আলাদা route, controller, model structure রাখা যায়               |

---

## 📱 Real-world Scenario:

### Facebook:

> browser থেকে request: `GET /feed`  
> Node.js বুঝে নেয় ইউজার কে, তার বন্ধুদের পোস্ট কী, কী সাজিয়ে দিতে হবে  
> তারপর response: `HTML/CSS/JSON`

### Instagram:

> mobile app থেকে request: `GET /user/123/profile`  
> Node.js DB দেখে profile data নিয়ে JSON আকারে পাঠিয়ে দেয়

---

## 🖼️ সহজ তুলনা:

> 🔧 **Physical server** = দোকান খোলার জন্য জায়গা  
> 🚪 **Node.js server** = দোকানে বসে থাকা কর্মচারী, যে জানে কীভাবে কাস্টমারকে সাহায্য করতে হয়

---

## ✅ Node.js Server না থাকলে?

| Request আসবে? | হ্যাঁ — Browser থেকে |
| কে ধরবে? | ❌ কেউ না (Node.js না থাকলে) |
| Result আসবে? | ❌ না — কারণ কেউ তো process করছেই না |

---

## 📌 সহজে মনে রাখার টিপস:

> **"Physical Server হলো কোথায় চালাবো"**  
> **"Node.js Server হলো কী চালাবো"**

```bash
# উদাহরণ: Render বা Heroku তে Node.js app deploy করলে
# তোমার কোড চলবে সেখানে — Physical server এ host হয়ে
```

---

## 🌐 Physical Server-এ কি আমরা File/Code Deploy করি?

---

### ❓ প্রশ্ন:

> **“Physical server-এ কি আমরা আমাদের file/code deploy করি?”**

---

## 🔥 সংক্ষিপ্ত উত্তর:

**হ্যাঁ — Physical Server বা Cloud Server-এ আমরা আমাদের Node.js কোড (server code, frontend files) ডিপ্লয় করি**, যেন সেটা ইন্টারনেট থেকে request পেয়ে run করতে পারে।

---

## 🧱 Physical Server (বা Cloud Server) কী?

এটা এমন একটি **কম্পিউটার বা virtual machine**, যেটা ২৪ ঘণ্টা চালু থাকে ইন্টারনেট সংযোগে।

### ✅ উদাহরণ:

- AWS EC2
- DigitalOcean Droplet
- Heroku, Vercel, Render (fully managed cloud)
- নিজের Computer (local server)

---

## 🧑‍💻 Node.js App বা Code কীভাবে Deploy করি?

তুমি যখন `Node.js` দিয়ে কোনো ওয়েব অ্যাপ বানাও, তখন তোমার থাকে:

- `.js` ফাইল
- API route
- server config
- frontend ফাইল ইত্যাদি

**এই ফাইলগুলো আমরা Physical Server-এ পাঠাই (upload/deploy করি)**।

---

### 🚀 Deploy মানে কী?

> তোমার কোড ফাইলগুলো সার্ভারে কপি করা + সেখানে চালানো + ওয়েব থেকে access-যোগ্য করে তোলা।

---

## 🛠 বাস্তব উদাহরণ:

ধরো তোমার একটা Node.js অ্যাপ আছে:

```
project/
├── index.js
├── package.json
├── routes/
└── public/
```

তুমি এটা `DigitalOcean` বা `Render`-এ **deploy** করলে:

- এই সব ফাইল সার্ভারে চলে যাবে
- সার্ভারে Node.js installed থাকবে
- তুমি `node index.js` বা `npm start` দিয়ে সার্ভার চালু করবে
- এখন কেউ `https://yourdomain.com` এ হিট করলে, তোমার অ্যাপ response দেবে

---

## 📦 সার্ভারে কোড কীভাবে পাঠাই?

| উপায়         | টুল                                      |
| ------------ | ---------------------------------------- |
| Command Line | `scp`, `rsync`, `ssh`                    |
| Git          | GitHub থেকে `git pull`                   |
| Deploy Tool  | Heroku CLI, Vercel CLI, Render dashboard |
| FTP/SFTP     | FileZilla, Cyberduck                     |

---

## 🎯 সংক্ষেপে মনে রাখার মতো:

| বিষয়               | ব্যাখ্যা                                             |
| ------------------ | ---------------------------------------------------- |
| 📁 কোড থাকবে       | তোমার লোকাল কম্পিউটারে তৈরি হবে                      |
| 🚀 Deploy করতে হবে | সার্ভারে পাঠিয়ে ওখানে চালাতে হবে                     |
| 🌍 Access হবে      | ব্রাউজার বা মোবাইল থেকে request এলে server সেটা ধরবে |

---

## 📦 Node.js-এ `export`, `export default`, `module.exports` — সবকিছু একসাথে ব্যাখ্যা

---

### ❓প্রশ্ন:

> **“Node.js এ export default, export, module.exports — এগুলোর কাজ কী?”**

---

## 🧠 সংক্ষিপ্ত উত্তর:

Node.js-এ বিভিন্ন ফাইল বা মডিউল তৈরি করলে, আমরা চাই সেই ফাইলের কিছু অংশ (function, object, class) অন্য জায়গায় **import** করে ব্যবহার করতে।

তার জন্যই লাগে ➜ **`export`** (JS মডিউল সিস্টেম) বা **`module.exports`** (CommonJS সিস্টেম)।

---

## 🧩 দুই রকমের Module System:

| ধরন       | ব্যবহার হয়                             | ফাইল টাইপ                    |
| --------- | -------------------------------------- | ---------------------------- |
| CommonJS  | `require()` + `module.exports`         | `.js`                        |
| ES Module | `import` + `export` / `export default` | `.mjs` বা `"type": "module"` |

---

## 🧱 ১. `module.exports` (CommonJS Style — Default in Node.js)

### 🔧 Export:

```js
// file: calc.js
function add(a, b) {
  return a + b;
}

module.exports = add;
```

### 📥 Import:

```js
// file: app.js
const add = require("./calc");
console.log(add(2, 3)); // 👉 Output: 5
```

👉 এখানে পুরো ফাংশনটা `module.exports` এ দেওয়া হচ্ছে — তাই যিনি import করবেন, তিনি সরাসরি `add` ফাংশনটি পাবেন।

---

## 🧱 ২. `exports` (CommonJS Style — Named Exports)

```js
// file: math.js
exports.add = function (a, b) {
  return a + b;
};

exports.mul = function (a, b) {
  return a * b;
};
```

```js
// file: app.js
const math = require("./math");
console.log(math.add(5, 3)); // 👉 8
console.log(math.mul(5, 3)); // 👉 15
```

👉 এখানে `exports.add` ও `exports.mul` আলাদা করে export করা হয়েছে।

---

## 🧱 ৩. `export` / `export default` (ES Modules Style)

### 🧑‍💻 Export (Named and Default):

```js
// file: utils.mjs
export function sayHello() {
  console.log("Hello!");
}

export default function sayBye() {
  console.log("Bye!");
}
```

### 📥 Import:

```js
// file: app.mjs
import sayBye, { sayHello } from "./utils.mjs";

sayHello(); // 👉 "Hello!"
sayBye(); // 👉 "Bye!"
```

---

## 📌 পার্থক্য সংক্ষেপে:

| টপিক           | `module.exports` / `exports` | `export` / `export default` |
| -------------- | ---------------------------- | --------------------------- |
| সাপোর্ট        | Node.js (default)            | ES6 Module বা `.mjs`        |
| Import Style   | `require()`                  | `import`                    |
| Default Export | `module.exports = func`      | `export default func`       |
| Named Export   | `exports.name = val`         | `export function name() {}` |

---

## 🧠 কখন কোনটা ব্যবহার করবো?

| পরিস্থিতি                      | সঠিক পছন্দ                  |
| ------------------------------ | --------------------------- |
| পুরাতন Node.js প্রকল্প         | `module.exports`            |
| আধুনিক JavaScript / TypeScript | `export` / `export default` |
| একটাই জিনিস export করতে চাই    | `default` ব্যবহার করা ভাল   |

---

## 🎯 সহজে মনে রাখার টিপস:

> 🔹 `module.exports = ...` → পুরো কিছু পাঠাও  
> 🔹 `exports.abc = ...` → অনেক কিছু আলাদা করে পাঠাও  
> 🔹 `export default ...` → ES6 style একটাই জিনিস পাঠাও  
> 🔹 `export { a, b }` → অনেক named export পাঠাও

---

## 🧪 Bonus: Mixed mistake তুমি যেন না করো!

```js
// ❌ ভুল: একই সাথে দুইটা ব্যবহার করছো
module.exports = {
  a: 1,
};

exports.b = 2; // 👉 এটি আর কাজ করবে না!
```

> কারণ `module.exports` দিলে `exports` আর কাজ করে না।

---

## 🧵 শেষ কথা:

> Node.js-এ code ভাগ করে ব্যবহার করার জন্য export / import ব্যবস্থাই backbone।  
> তুমি চাইলে CommonJS (default) বা modern ES Modules — যেকোনোটি ব্যবহার করতে পারো।

---

## 🔍 কোনটা ES6, কোনটা CommonJS? — Import/Export পার্থক্য ব্যাখ্যা

---

## ❓প্রশ্ন:

> **"আমি কিভাবে বুঝবো import/export ES6-এর, আর require/module.exports CommonJS-এর?"**

---

## 🧠 সংক্ষিপ্ত উত্তর:

| Syntax              | ব্যবহৃত প্রযুক্তি | মডিউল টাইপ               |
| ------------------- | ----------------- | ------------------------ |
| `require()`         | CommonJS          | `.js` (default)          |
| `module.exports`    | CommonJS          | `.js` (default)          |
| `import` / `export` | ES6 (ES Modules)  | `.mjs` বা `type: module` |

---

## 📦 CommonJS (পুরাতন, Node.js এর built-in)

### ✅ চেনার উপায়:

```js
const something = require('./module');
module.exports = function () { ... };
```

### 🧾 ব্যাখ্যা:

- Node.js শুরু থেকেই এই পদ্ধতি ব্যবহার করে
- শুধুমাত্র Node.js এ চলে (Browser এ না)
- `.js` ফাইলেই চালানো যায়, আলাদা config লাগে না

---

## 🌐 ES6 Modules (আধুনিক JS standard)

### ✅ চেনার উপায়:

```js
import something from './module.js';
export default function () { ... }
export function helper() { ... }
```

### 🧾 ব্যাখ্যা:

- এটি হলো **ECMAScript 2015 (ES6)** এর অংশ
- Node.js v12+ এ সাপোর্ট করে, কিন্তু কিছু config দরকার হয়
- Browser এ সরাসরি চলে

---

## 🔧 Node.js এ ES6 Module ব্যবহার করতে হলে কী করতে হবে?

তোমার Node.js প্রোজেক্টে ES6 module চালাতে চাইলে:

### 🛠 উপায় ১: `.mjs` extension দাও

```bash
filename: utils.mjs
```

```js
// utils.mjs
export function hello() { ... }
```

### 🛠 উপায় ২: `package.json` এ type যুক্ত করো

```json
// package.json
{
  "type": "module"
}
```

```js
// এখন .js ফাইলেও import/export চলবে
import { hello } from "./utils.js";
```

---

## 🎯 তুলনা টেবিল:

| বৈশিষ্ট্য        | CommonJS (require)            | ES6 Module (import/export)           |
| ---------------- | ----------------------------- | ------------------------------------ |
| Syntax           | `require()`, `module.exports` | `import`, `export`, `export default` |
| ডিফল্ট কোথায় চলে | Node.js                       | Browser + Node.js v12+               |
| ফাইল টাইপ        | `.js`                         | `.mjs` বা `.js` with `type:module`   |
| Dynamic Import   | ❌ না                         | ✅ `import()` async ভাবে করা যায়     |
| Tree Shaking     | ❌ না                         | ✅ হ্যাঁ (Webpack/ESBuild-friendly)  |

---

## 🖼️ উদাহরণে পার্থক্য:

### ✅ CommonJS:

```js
// calc.js
function add(a, b) {
  return a + b;
}
module.exports = add;

// app.js
const add = require("./calc");
console.log(add(2, 3));
```

### ✅ ES6 Module:

```js
// calc.mjs
export function add(a, b) {
  return a + b;
}

// app.mjs
import { add } from "./calc.mjs";
console.log(add(2, 3));
```

---

## 🔁 Browser এর জন্য?

| Feature              | CommonJS    | ES6 Modules                 |
| -------------------- | ----------- | --------------------------- |
| Browser Support      | ❌ না (নেই) | ✅ Chrome, Firefox          |
| সরাসরি import script | ❌ না       | ✅ `<script type="module">` |

```html
<script type="module">
  import { myFunc } from "./module.js";
</script>
```

---

## 🧩 মনে রাখার সহজ উপায়:

> 📦 CommonJS = Node.js only = `require()`  
> 🌐 ES6 Module = Modern JS (Browser + Node) = `import/export`

---

## 🧠 মনে রাখার টিপস:

> 🔹 `.js` = CommonJS  
> 🔹 `.mjs` বা `"type": "module"` = ES6 Module  
> 🔹 Browser এ চালাতে চাইলে → `import/export` ব্যবহার করো  
> 🔹 Node.js এ default → `require/module.exports`

---

## ✅ শেষ কথা:

- **Node.js এ দুইটাই চলে**, কিন্তু একসাথে মেশালে সমস্যা হয়
- নতুন প্রোজেক্টে গেলে **ES6 Modules (import/export)** use করাই ভাল
- পুরোনো বা লাইব্রেরি heavy প্রোজেক্টে **require/module.exports** ই standard

---
