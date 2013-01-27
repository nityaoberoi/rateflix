from settings import *

DEBUG = False
PRODUCTION = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heroku_3000ec83c1561da',
        'USER': 'b3fc7ab06a9e40',
        'PASSWORD': '5f5ced39',
        'HOST': 'us-cdbr-east-03.cleardb.com',
        'PORT': '3306',
    }
}