// import http from "http";
// import requestHandaler from "./routes.js";

// const server = http.createServer(requestHandaler);

// server.listen(3001);

import express from "express";
import admin_router from "./routes/admin.js";
import shop_router from "./routes/shop.js";
import { fileURLToPath } from "url";

// Get current file path
const __filename = fileURLToPath(import.meta.url);

// Get current directory path (similar to __dirname in CommonJS)
const __dirname = path.dirname(__filename);
import path from "path";

const app = express();
app.use(express.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, "public")));

app.use(admin_router);
app.use(shop_router);

app.use("/hello", (req, res, next) => {
  res.send("Hello");
});

app.listen(3000);
