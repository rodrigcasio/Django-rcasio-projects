# PostgreSQL
SECRET_KEY = 'A_TEMPORARY_SECRET_KEY_FOR_THIS_PROJECT'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INSTALLED_APPS = (
    'related_objects',
)

# 3. DATABASE CONFIGURATION (Use your dedicated credentials)
DATABASES = {
    'default': {
        # Using 'postgresql' for psycopg3 (psycopg-binary)
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'lab_3_db',
        'USER': 'lab_3_user',
        'PASSWORD': 'Kumon7700',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
