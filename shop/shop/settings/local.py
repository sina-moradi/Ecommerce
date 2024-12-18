from .base import *

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECRET_KEY = 'django-insecure-(#1sh(=1_d878crd(g#6qsa4dyjkc4x6)8sgu##pimr!&ueo_0'

# ALLOWED_HOSTS = env_setting("ALLOWED_HOSTS").split(",")
ALLOWED_HOSTS = ['*']
# CSRF_TRUSTED_ORIGINS = env_setting("CSRF_TRUSTED_ORIGINS").split(",")
CSRF_TRUSTED_ORIGINS = (
    'https://localhost:3000',
)
# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'shop',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


