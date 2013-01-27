from settings import *

DEBUG = False
PRODUCTION = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heroku_99428f7c54091d9',
        'USER': 'b9808af61a74e3',
        'PASSWORD': 'f25efa6c',
        'HOST': 'us-cdbr-east-03.cleardb.com',
        'PORT': '3306',
    }
}