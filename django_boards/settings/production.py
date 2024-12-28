from .base import *

# using decouple to point to ALLOWED_HOSTS env var on render
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

MEDIA_ROOT_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MEDIA_ROOT = os.path.join(MEDIA_ROOT_BASE_DIR, 'mediafiles')

# Render database
# using decouple
DATABASES = {
    "default": dj_database_url.config(default=config("DATABASE_URL"), conn_max_age=600),
}

# This production code might break development mode, so we check whether we're in DEBUG mode
# Tell Django to copy static assets into a path called `static` (this is specific to Render)
STATIC_ROOT = BASE_DIR / '../staticfiles'

