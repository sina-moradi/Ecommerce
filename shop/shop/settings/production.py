from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env_setting('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = env_setting("ALLOWED_HOSTS").split(",")
CSRF_TRUSTED_ORIGINS = env_setting("CSRF_TRUSTED_ORIGINS").split(",")

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env_setting('DB_NAME'),
        'USER': env_setting('DB_USER'),
        'PASSWORD': env_setting('DB_PASSWORD'),
        'HOST': env_setting('DB_HOST'),
        'PORT': env_setting('DB_PORT'),
    }
}

