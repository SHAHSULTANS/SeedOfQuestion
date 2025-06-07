// import http from "http";
// import requestHandaler from "./routes.js";

// const server = http.createServer(requestHandaler);

// server.listen(3001);

import express from "express";
import admin_router from "./routes/admin.js";
import shop_router from "./routes/shop.js";

const app = express();

app.use(admin_router);
app.use(shop_router);

app.use("/hello", (req, res, next) => {
  res.send("Hello");
});

app.listen(3000);
