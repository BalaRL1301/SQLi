package com.example.demo;

import org.springframework.web.bind.annotation.*;
import java.sql.*;

@RestController
public class LoginController {

    @PostMapping("/login")
    public String login(@RequestParam String username, @RequestParam String password) {
        try {
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/sql_injection_demo", "root", "PB@1301x2805");
            Statement stmt = con.createStatement();
            String query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'";
            ResultSet rs = stmt.executeQuery(query);
            if (rs.next()) {
                return "Welcome " + username;
            }
        } catch (Exception e) {
            return "Error: " + e.getMessage();
        }
        return "Login failed";
    }
}