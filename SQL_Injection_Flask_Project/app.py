from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# Simple in-memory SQLite DB setup
def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    c.execute("DELETE FROM users")
    c.execute("INSERT INTO users VALUES ('admin', 'admin123')")
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        # Vulnerable query

        #query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        
        #result = c.execute(query).fetchone()
         c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password)) #changed query
         result = c.fetchone() #changed query
        conn.close()
        if result:
            message = f"Welcome {username}!"
        else:
            message = "Login Failed."
    return render_template_string('''
        <h2>Login</h2>
        <form method="post">
            Username: <input name="username"><br>
            Password: <input name="password"><br>
            <input type="submit" value="Login">
        </form>
        <p>{{ message }}</p>
    ''', message=message)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)