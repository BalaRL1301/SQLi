Django SQL Injection Demo (Raw SQL Vulnerability)

1. Prerequisites:
   - Python 3, pip, and virtualenv
   - Django installed: pip install django

2. Setup:
   django-admin startproject sqldemo
   cd sqldemo
   python manage.py startapp core

3. Replace core/views.py and core/urls.py with the provided files.
   Update sqldemo/settings.py and sqldemo/urls.py to include 'core'.

4. Create a superuser for demo:
   python manage.py migrate
   python manage.py createsuperuser

5. Run the server:
   python manage.py runserver

6. Open: http://localhost:8000
   Try:
   Username: youradminusername' --
   Password: [blank]

This will bypass the login check if raw SQL is used unsafely.

Fix:
Use parameterized queries or Django ORM.