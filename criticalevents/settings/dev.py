from .base import *

DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': BASE_DIR / 'db.sqlite3',
    },
    'mysql':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'ssibuyi',
        'PASSWORD': 'Asd1!2@2',
        'HOST': '10.100.100.137',
        'PORT': ''
    }
}