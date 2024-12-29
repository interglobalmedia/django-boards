from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
# using pyhon-dotenv
DEBUG = os.getenv('DEBUG')

# using decouple to point to ALLOWED_HOSTS env var locally
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

# For user uploaded files locally
# MEDIA_ROOT = os.path.join(BASE_DIR, "../media")

MEDIA_ROOT = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'media'))
print(MEDIA_ROOT, 'media root in development')

# Local Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "../db.sqlite3",
    }
}

# Local only
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "../static"),
]