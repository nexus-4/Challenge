# Simple HTTP Server

This project contains a basic HTTP server implemented using Node.js's built-in `http` module.

## Description

The HTTP server listens on port 3000 and handles requests to two different routes: `/` and `/about`.

- When a request is made to the root route (`/`), the server responds with a simple HTML message saying "Hello There!".
- When a request is made to the `/about` route, the server responds with a plaintext message saying "About Page".
- For any other route, the server responds with a plaintext message saying "404 Not Found".

## Usage

To run the HTTP server, execute the following steps:

1. Clone the repository to your local machine: git clone <repository_url> ;
2. Open the file: cd <namesfiles>
3. Run server: node server.js
4. Once the server is running, you can send HTTP requests to http://localhost:3000 to access the defined routes.
