import express from "express";

// Required in ES6 modules
import path from "path";
import { fileURLToPath } from "url";

// Get current file path
const __filename = fileURLToPath(import.meta.url);

// Get current directory path (similar to __dirname in CommonJS)
const __dirname = path.dirname(__filename);

const router = express.Router();

router.get("/add-product", (req, res, next) => {
  res.sendFile(path.join(__dirname, "../", "views", "admin_page.html"));
});

router.post("/add-product", (req, res, next) => {
  console.log(req.body);
  res.redirect("/");
});

export default router;
