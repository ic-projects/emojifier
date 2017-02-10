var express = require('express');
var net = require('net');
var router = express.Router();

/* POST users listing. */
router.post('/', function(req, res, next) {
    var message = req.body.message.toLowerCase().replace(/[^a-z ]/gi,'');

    var client = new net.Socket();
    client.connect(3000, 'localhost', function() {
        console.log("Connected.  " + message );
        client.write(message);
    });

    client.on('data', function(data) {
        res.send(data.toString());
    });

    client.on('close', function() {
        console.log("Connection closed.");
    });
});

module.exports = router;
