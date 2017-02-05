var express = require('express');
var path = require('path');
var favicon = require('serve-favicon');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');

var index = require('./routes/index');
var users = require('./routes/users');

var app = express();

/***********************************************************************************************************************
 *  RESTful API for requesting DB requests
 *  Call mfournial before any modification
 **********************************************************************************************************************/

// DB MIKE Serving client RUN
var fs = require("fs");



// Get the json database file to be read by fs
// Prints the entire JSON DB visiting '/listItems'
app.get('/listItems', function (req, res) {
    fs.readFile( __dirname + "/Mike/" + "items.json", 'utf8', function (err, data) {
        console.log( data );
        res.end( data );
    });
});

// Do some AJAX Requesting to get the user's input
// The var must contain an object of JSON the key is irrelevant
// fields are :input -> stringProcessable, :output -> stringProcessable
// var newItem = {
//     "foo" : {
//         "input": `INPUT TEXT`,
//         "output": `OUTPUT TEXT`
//     }
// }

var newUser = {
    "foo": {
        "input": "test11ADD",
        "output": "test11ADDoutput"
    }
};


app.post('/addUser', function (req, res) {
    fs.readFile( __dirname + "/Mike/" + "items.json", 'utf8', function (err, data) {
        // Gets the db
        data = JSON.parse(data);

        var keys = [];
        for (var k in newUser) {
          keys.push(k);
        }
        data[keys[0]] = newUser[keys[0]];

        console.log(data);
        res.send(JSON.stringify(ds));
    });
});

/***********************************************************************************************************************
 *   END OF RESTful API
 *   For your pleasure
 *   Hope you're not reading this at 2am
 **********************************************************************************************************************/


// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

// uncomment after placing your favicon in /public
//app.use(favicon(path.join(__dirname, 'public', 'favicon.ico')));
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', index);
app.use('/users', users);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  var err = new Error('Not Found');
  err.status = 404;
  next(err);
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
