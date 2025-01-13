from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
# using pyhon-dotenv
DEBUG = True

# using decouple to point to ALLOWED_HOSTS env var locally
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

# For user uploaded files locally
MEDIA_ROOT = os.getenv("MEDIA_ROOT")

print(MEDIA_ROOT, "media root in development")

WSGI_APPLICATION = "django_boards.wsgi.application"

# correct absolute path in which db.sqlite3 resides
CURRENT_DIR = "/Users/mariacam/Python-Development/django-boards/"

# Local Database. Comment out before deploying to production
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": CURRENT_DIR + "db.sqlite3",
#     }
# }

# Local only
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "../static"),
]
