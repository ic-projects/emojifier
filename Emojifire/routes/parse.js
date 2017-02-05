var express = require('express');
var router = express.Router();

/* POST users listing. */
router.post('/', function(req, res, next) {
    var message = req.body.message;
    bgProc.stdin.write(message + "\n");
    bgProc.stdin.on('data', function(data) {
      console.log(data);
    });

    // bgProc.stdin.write("Test\n");
    // bgProc.stdout.on('data', function(data){
    //     console.log(data.toString());
    // });
    res.send(message);
});

module.exports = router;
