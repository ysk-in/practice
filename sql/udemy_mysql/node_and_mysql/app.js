var dotenv = require("dotenv").config();
var faker = require("faker");
var mysql = require("mysql");

/*
node_and_mysql フォルダ直下に .env ファイルが以下内容で必要
DB_HOST=<DB接続するHOST e.g. localhost>
DB_USER=<DB接続に使用するユーザ名>
DB_PASS=<DB接続に使用するパスワード>
... dotenv.env.XXX で参照してるプロパティの定義が必要
*/

if (dotenv.error) {
  throw dotenv.error;
}
console.log(dotenv.parsed);

var con = mysql.createConnection({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASS,
  database: "join_us"
});

// GET USERS COUNT
// var sql = "SELECT COUNT(*) as total from users";
// con.query(sql, function(err, results, fields) {
//   if (err) throw err;
//   console.log(results[0].total);
// });

// INSERT A USER
// var person = {email: faker.internet.email()};
// var sql = "INSERT INTO users SET ?";
// var result = con.query(sql, person, function(err, results, fields) {
//   if (err) throw err;
//   console.log(results);
// });
// console.log(resuql.sql);

var data = [];
for (var i = 0; i < 500; i++) {
  data.push([faker.internet.email(), faker.date.past()]);
}
var sql = "INSERT INTO users (email, created_at) VALUES ?";
con.query(sql, [data], function(err, result) {
  console.log(err);
  console.log(result);
});

con.end();
