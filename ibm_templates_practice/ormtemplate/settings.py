# settings.py
# 1. SECRET KEY (Required by Django)
SECRET_KEY = 'A_TEMPORARY_SECRET_KEY_FOR_THIS_PROJECT'

# 2. INSTALLED APPS (Register your standalone app)
INSTALLED_APPS = (
    'standalone',
)

# 3. DATABASE CONFIGURATION (Use your dedicated credentials)
DATABASES = {
    'default': {
        # Using 'postgresql' for psycopg3 (psycopg-binary)
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'orm_template_db', 
        'USER': 'orm_user', 
        'PASSWORD': 'Kumon7700', # <-- UPDATE THIS
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
