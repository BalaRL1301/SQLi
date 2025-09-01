const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql2');
const app = express();

app.use(bodyParser.urlencoded({ extended: false }));

const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'PB@1301x2805',
  database: 'sql_injection_demo'
});

db.connect();

app.get('/', (req, res) => {
  res.send(`<form method="POST" action="/login">
              Username: <input name="username"><br>
              Password: <input name="password"><br>
              <input type="submit" value="Login">
            </form>`);
});

app.post('/login', (req, res) => {
  const username = req.body.username;
  const password = req.body.password;
  const query = `SELECT * FROM users WHERE username='${username}' AND password='${password}'`;
  db.query(query, (err, results) => {
    if (results.length > 0) {
      res.send("Welcome " + username);
    } else {
      res.send("Login failed");
    }
  });
});

app.listen(3000, () => console.log("Server started on port 3000"));


