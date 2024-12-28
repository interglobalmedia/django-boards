from .base import *
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

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())