# PostgreSQL

SECRET_KEY = 'A_TEMPORARY_SECRET_KEY_FOR_THIS_PROJECT'

INSTALLED_APPS = (
    'crud',
)

# 3. DATABASE CONFIGURATION (Use your dedicated credentials)
DATABASES = {
    'default': {
        # Using 'postgresql' for psycopg3 (psycopg-binary)
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'lab_crud_template_db',
        'USER': 'lab_crud_user',
        'PASSWORD': 'Kumon7700',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
