from .base import *

DEBUG = True


ALLOWED_HOSTS = ["localhost", "127.0.0.1"]



# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

os.environ['DJANGO_PORT'] =  '3000'