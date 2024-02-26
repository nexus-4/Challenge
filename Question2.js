//Simple HTTP server
//import module
const http = require('http');
const PORT = 3000;

//Create server
const server = http.createServer(function (req, res) {
    // Check if the request URL is '/'
    if (req.url === '/') {
        res.write('<h1>Hello There!</h1>')
    }
    // Check if the request URL is '/about'
    if (req.url === '/about') {
        res.write('About Page')
    }
    else {
        //route 404 not found
        res.write('404 Not Found')
    }
    res.end();

});


//start the server and listen on the specified port
server.listen(PORT, () => {
    console.log('Listening on port 3000...')
});