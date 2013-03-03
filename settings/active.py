# from settings.production import *
from settings.local import *

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
AWS_S3_CUSTOM_DOMAIN = 'http://localhost:8000/media'
THUMBOR_BASE_URL = 'http://0.0.0.0:8888'
THUMBOR_KEY = b'0e868ea0-0974-4dbb-b967-e30c8952dd1d'
