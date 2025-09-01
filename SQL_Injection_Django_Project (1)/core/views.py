from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection

def login_view(request):
    message = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        with connection.cursor() as cursor:
            query = f"SELECT * FROM auth_user WHERE username='{username}' AND password='{password}'"
            cursor.execute(query)
            row = cursor.fetchone()
            if row:
                message = f"Welcome {username}"
            else:
                message = "Login failed"
    return HttpResponse(f'''
        <form method="POST">
            Username: <input name="username"><br>
            Password: <input name="password"><br>
            <input type="submit" value="Login"><br>
        </form>
        <p>{message}</p>
    ''')