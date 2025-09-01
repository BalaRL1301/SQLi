Instructions for Spring Boot SQL Injection Demo

1. Prerequisites:
   - Java 11+ and Maven
   - MySQL running on localhost

2. Create database and table in MySQL:
   CREATE DATABASE sql_injection_demo;
   USE sql_injection_demo;
   CREATE TABLE users (username VARCHAR(50), password VARCHAR(50));
   INSERT INTO users VALUES ('admin', 'admin123');

3. Project Files:
   This example includes a basic vulnerable repository with hardcoded SQL query.

4. To Run:
   - Place the files in an IDE (like IntelliJ)
   - Run as a Spring Boot application
   - Visit: http://localhost:8080/login

5. Try:
   it does not have the user interface for give the input validations so we need to do using the curl in terminal

   with username and password
   curl -X POST "http://localhost:8080/login" -d "username=admin&password=admin123"

   attempting with the sql injection
   curl -X POST "http://localhost:8080/login" -d "username=admin' OR '1'='1" -d "password=""


6. Fix:
   Replace Statement with PreparedStatement.



before

Statement stmt = con.createStatement();
String query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'";
ResultSet rs = stmt.executeQuery(query);



after

String query = "SELECT * FROM users WHERE username = ? AND password = ?";
PreparedStatement pstmt = con.prepareStatement(query);
pstmt.setString(1, username);
pstmt.setString(2, password);
ResultSet rs = pstmt.executeQuery();

