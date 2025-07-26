কনসেপ্ট বোঝা অনেক সহজ হয় যদি আমরা বাস্তব উদাহরণ দিয়ে ব্যাখ্যা করি – বিশেষ করে **ওয়েব অ্যাপ্লিকেশন ভিত্তিক**। এবার আমি **Authentication** এবং **Authorization**–এর প্রতিটি টাইপকে **বাস্তব ওয়েব অ্যাপ্লিকেশন ভিত্তিক উদাহরণ** দিয়ে একদম প্রফেশনালভাবে ব্যাখ্যা করছি।

---

## 🔐 **Authentication (প্রমাণীকরণ) — "তুমি কে?"**

ওয়েব অ্যাপে ইউজার যখন লগইন করে, তখন আমরা যাচাই করি সে প্রকৃত ইউজার কি না। নিচে বিভিন্ন পদ্ধতি ও উদাহরণ:

---

### ১. **Username + Password Authentication**

#### ✅ উদাহরণ:

> তুমি `example.com` ওয়েবসাইটে রেজিস্টার করেছো। এখন লগইনের সময় ইউজারনেম/ইমেইল + পাসওয়ার্ড দিয়ে ঢুকো।

🔹 **কোথায় দেখা যায়:** প্রায় সব ওয়েবসাইটে (Facebook, Gmail, LinkedIn)

🔐 দুর্বল পয়েন্ট:

* যদি পাসওয়ার্ড ফাঁস হয়, অ্যাকাউন্ট হ্যাক হতে পারে।

---

### ২. **Two-Factor Authentication (2FA)**

#### ✅ উদাহরণ:

> তুমি Gmail-এ লগইন করেছো পাসওয়ার্ড দিয়ে। এরপর Google তোমার মোবাইলে OTP পাঠাল — এই OTP না দিলে অ্যাকসেস পাবে না।

🔹 **কোথায় দেখা যায়:** Gmail, Facebook, GitHub, ব্যাংক অ্যাপ

🔐 সুবিধা:

* পাসওয়ার্ড ফাঁস হলেও OTP ছাড়া কেউ ঢুকতে পারবে না।

---

### ৩. **OAuth (Third-party login)**

#### ✅ উদাহরণ:

> তুমি একটি নতুন নিউজ ওয়েবসাইটে ঢুকতে চাইছো। কিন্তু রেজিস্ট্রেশন না করেই, “Login with Google” বাটনে ক্লিক করছো।

🔹 **কোথায় দেখা যায়:** Medium.com, Quora, Trello

🔐 সুবিধা:

* ইউজারের জন্য ঝামেলাহীন।
* সার্ভার ইউজারের Google অ্যাকাউন্ট ব্যবহার করে তার পরিচয় যাচাই করে।

---

### ৪. **Token-based Authentication (JWT)**

#### ✅ উদাহরণ:

> তুমি যখন e-commerce ওয়েবসাইটে লগইন করো, তখন সার্ভার তোমাকে একটা **JWT Token** দেয়। এরপর তুমি যখন যেকোনো পেজে যাও (order history, profile), সেই টোকেন দেখিয়ে তুমি বলে দাও — "আমি আগেই প্রমাণ করেছি, এটা আমার পরিচয়।"

🔹 **ব্যবহার হয়:** SPA (Single Page Applications), API calls

🔐 সুবিধা:

* Stateless এবং scalable।

---

### ৫. **Biometric Authentication**

#### ✅ উদাহরণ:

> তুমি যখন তোমার মোবাইল ব্রাউজারে ব্যাংক অ্যাপে ঢুকতে চাও, তখন Face ID বা Fingerprint চাই।

🔹 **কোথায় দেখা যায়:** Mobile banking, Apple Pay, Google Pay

---

## ✅ **Authorization (অনুমোদন) — "তুমি কী করতে পারো?"**

একবার ইউজার লগইন করলে, সে কী অ্যাক্সেস করতে পারবে সেটা নিয়ন্ত্রণ করা হয় Authorization দিয়ে।

---

### ১. **Role-Based Access Control (RBAC)**

#### ✅ উদাহরণ:

> তুমি `admin.panel.com` ওয়েব অ্যাপে ঢুকেছো। তুমি যদি **Admin** হও, তাহলে User Delete অপশন দেখতে পাবে। যদি **Editor** হও, তাহলে কেবল পোস্ট এডিট করতে পারবে।

🔹 **ব্যবহার হয়:** CMS (Content Management System), Internal Dashboard

---

### ২. **Attribute-Based Access Control (ABAC)**

#### ✅ উদাহরণ:

> একটি কোম্পানির ফাইল ম্যানেজমেন্ট সিস্টেমে, শুধু সেই ইউজারই রিপোর্ট ডাউনলোড করতে পারবে, যার **department = finance** এবং **location = head office**।

🔹 **ব্যবহার হয়:** বড় কর্পোরেট অ্যাপে, যেখানে complex শর্ত থাকে।

---

### ৩. **Access Control List (ACL)**

#### ✅ উদাহরণ:

> তোমার Google Drive-এ কোনো ফাইল শেয়ার করেছো — তুমি নির্দিষ্ট করে দাও:
>
> * Anik → can view
> * Sumi → can edit
> * Rafi → no access

🔹 **ব্যবহার হয়:** Cloud services, File-sharing apps

---

### ৪. **Policy-Based Access Control (PBAC)**

#### ✅ উদাহরণ:

> Amazon বা ERP সিস্টেমে এমন policy থাকতে পারে:
> "Sales department-এর কেউ ৯টা থেকে ৬টার মধ্যে ইনভয়েস জেনারেট করতে পারবে, তবে ছুটির দিনে নয়।"

🔹 **ব্যবহার হয়:** High-security enterprise অ্যাপস।

---

## 🧠 Summary Chart:

| ধরন            | Authentication উদাহরণ                  | Authorization উদাহরণ                             |
| -------------- | -------------------------------------- | ------------------------------------------------ |
| Password-based | Gmail-এ ইমেইল + পাসওয়ার্ড             | Only verified users can comment                  |
| 2FA            | OTP via SMS in banking app             | High-value transactions require manager approval |
| OAuth          | Login with Google in Medium            | Google account holders can't change others’ data |
| JWT            | SPA app token use (e.g., React + Node) | Token অনুযায়ী API endpoint এক্সেস করা যায়        |
| Biometric      | Fingerprint in Mobile App              | Only device owner can transfer funds             |
| RBAC           | User logged in                         | Admin can delete, editor can only edit           |
| ABAC           | Location-based login                   | Only users in UK can view this feature           |
| ACL            | Google Drive sharing                   | Only listed people can access files              |

---

## 🔚 শেষ কথা:

Authentication বলছে: **"তুমি কে?"**
Authorization বলছে: **"তুমি কী করতে পারো?"**


