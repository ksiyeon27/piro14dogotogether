from .base import *

DEBUG = False 

ALLOWED_HOSTS = ['dogotogether.tk']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'name',
        'USER': 'user',
        'PASSWORD': 'password'
        
    }   
}
