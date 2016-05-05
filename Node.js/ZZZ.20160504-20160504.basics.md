```
var http = require('http');
var server = http.createServer();

var handler = function(req, res) {
  res.writeHead(200, {});
  res.end('Hello World!');
};

server.on('request', handler);

server.listen(3000);
```

```
var http = require('http');

var opts = {
  host: 'www.google.com',
  port: 80,
  url: '/',
  method: 'GET'
};

var req = http.request(opts, function(res) {
  console.log(res);

  res.setEncoding('utf8');

  res.on('data', function(data) {
    console.log(data);
  });
});

req.write('my data');

req.write('more of my data');

req.end();
```

1. modules
  - Events
  - HTTP
  - HTTPS
  - URL
  - Cluster
  - Console
  - Crypto
  - Errors
  - fs
  - child_process
  - buffer
  - process
  - assert
  - node-db
  - Express
  

