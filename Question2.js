//Simple HTTP server
//initiate module
const http = require('http'); 
const port = 3000;

//Create server
const server = http.createServer(function (req, res) {
    if (req.url === '/') {
        res.write('Hello There!');
        res.end();
    }

});
server.listen(3000);
console.log('Listening on port 3000...')