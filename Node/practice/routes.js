import fs from "fs";

const requestHandaler = (req, res) => {
  const url = req.url;
  const method = req.method;

  if (url === "/") {
    // Respond with an HTML form
    res.setHeader("Content-Type", "text/html");
    res.write(`
          <html>
            <head><title>Enter Message</title></head>
            <body>
              <form action="/message" method="POST">
                <input type="text" name="message" placeholder="Enter something" />
                <button type="submit">Submit</button>
              </form>
            </body>
          </html>
        `);
    return res.end(); // End the response after sending form
  }

  // Optional: You can handle POST submission at /message route
  if (url === "/message" && method === "POST") {
    const body = [];
    req.on("data", (chunk) => {
      body.push(chunk);
    });

    req.on("end", () => {
      const parsedBody = Buffer.concat(body).toString();
      const message = parsedBody.split("=")[0];
      console.log("Form submitted:", message);
      fs.writeFileSync("./text.txt", message);

      // Respond with a thank you message
      res.setHeader("Content-Type", "text/html");
      res.write(
        `<html><body><h1>Thank you! Message received: ${message}</h1></body></html>`
      );
      res.end();
    });

    return;
  }

  res.setHeader("Content-Type", "text/html");
  res.write(`
          <html>
            <head><title>Enter Message</title></head>
            <body>
                <h1>Hello, this is a message page</h1>
              
            </body>
          </html>
        `);
  return res.end();
};

export default requestHandaler;
