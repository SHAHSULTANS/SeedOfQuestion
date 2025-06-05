import http from "http";
import requestHandaler from "./routes.js";

const server = http.createServer(requestHandaler);

server.listen(3001);
