Instructions for Node.js + MySQL SQL Injection Demo

1. Ensure MySQL is running and create the database and table:

CREATE DATABASE sql_injection_demo;
USE sql_injection_demo;
CREATE TABLE users (username VARCHAR(50), password VARCHAR(50));
INSERT INTO users VALUES ('admin', 'admin123');

2. Run these commands:
npm install express body-parser mysql
node app.js

3. Open browser at: http://localhost:3000

4. Try:
    Username: admin
    Password: admin123

Then try SQL Injection:
    Username: admin' --
    Password: [leave blank]
    # it's not working 


solution
    Username: admin' OR '1'=1--
    Password:[leave empty / type something] -> its gonna be a commands


code to prevent the SQL injection--

app.post('/login', (req, res) => {
  const username = req.body.username;
  const password = req.body.password;
  db.execute(
    'SELECT * FROM users WHERE username = ? AND password = ?', [username, password],
    (err, results) => {  
    if (results.length > 0) {
      res.send("Welcome " + username);
    } else {
      res.send("Login failed");
    }
  });
});