# PostgreSQL

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'Kumon7700',
        'HOST': 'postgres',
        'PORT': '5432',
    }
}

INSTALLED_APPS = {
    'standalone',
}

SECRET_KEY = 'SECRET_KEY for this Django project'

"""
This code adds 'standalone' app as an installed app and adds the default
database to be the pre-installed PostgreSQL created.
"""
