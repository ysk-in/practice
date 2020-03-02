var express = require("express");
var dotenv = require("dotenv").config();
var mysql = require("mysql");
var bodyParser = require("body-parser");

if (dotenv.error) throw dotenv.error;
console.log(dotenv.parsed);

var con = mysql.createConnection({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASS,
  database: "join_us"
});

var app = express();
app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(__dirname + "/public"));

app.get("/", function(req, res) {
  var sql = "SELECT COUNT(*) AS count FROM users";
  con.query(sql, function(err, results) {
    if (err) throw err;
    var count = results[0].count;
    res.render("home", { count: count });
  });
});

app.post("/register", function(req, res) {
  // console.log(req.body);
  var person = { email: req.body.email };
  var sql = "INSERT INTO users SET ?";
  var result = con.query(sql, person, function(err, results) {
    if (err) throw err;
    console.log(results);
    // res.send("Thanks for joining our wait list!");
    res.redirect("/");
  });
  //   get_home(req, res);
});

app.get("/joke", function(req, res) {
  var joke =
    "What do you call a dog that does magic tricks? A labracadabrador.";
  res.send(joke);
});

app.get("/random_num", function(req, res) {
  var num = Math.floor(Math.random() * 10 + 1);
  res.send("Your lucky number is " + num);
});

app.listen(8080, function() {
  console.log("Server running on 8080!");
});
