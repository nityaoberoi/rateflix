from os.path import abspath, dirname, join

DEBUG = False
TEMPLATE_DEBUG = DEBUG

LOCAL = False
PRODUCTION = False

PROJECT_ROOT = abspath(join(dirname(__file__), '../'))

ADMINS = (
    ('Nitya Oberoi', 'nitya.oberoi@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {}
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
SITE_ID = 1
USE_I18N = True
USE_L10N = True

STATIC_URL = '/static/'
MEDIA_ROOT = join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'

COMPRESS_ENABLED = True
COMPRESS_URL = MEDIA_URL
COMPRESS_OFFLINE = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = '+-f0f=h8o4z3!i9v+t*l4bq^&amp;531@ypxn(^mvty&)^i^q0$a-ef$8(nccr'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    join(PROJECT_ROOT, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    # 'django.core.context_processors.debug',
    # 'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    # 'django.core.context_processors.static',
    # 'django.contrib.messages.context_processors.messages',
)

INSTALLED_APPS = (

    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'compressor',
    'south',

    'rateflix',
)

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    'compressor.finders.CompressorFinder',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}