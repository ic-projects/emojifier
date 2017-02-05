var express = require('express');
var net = require('net');
var router = express.Router();

/* POST users listing. */
router.post('/', function(req, res, next) {
    var message = req.body.message.toLowerCase().replace(/[^a-z ]/gi,'');

    var client = new net.Socket();
    client.connect(8080, '129.31.212.117', function() {
        console.log("Connected.");
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
