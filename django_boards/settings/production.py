from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
# using environ
DEBUG = os.environ.get('DEBUG')

# using decouple to point to ALLOWED_HOSTS env var on render
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

# MEDIA_ROOT = os.environ.get("MEDIA_ROOT", "/opt/render/project/src/mediafiles")
MEDIA_ROOT = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'mediafiles'))
print(MEDIA_ROOT, "media root")


# Render database
# using decouple
# DATABASES = {
#     "default": dj_database_url.config(default=config("DATABASE_URL"), conn_max_age=600),
# }

# This production code might break development mode, so we check whether we're in DEBUG mode
# Tell Django to copy static assets into a path called `static` (this is specific to Render)
STATIC_ROOT = BASE_DIR / '../staticfiles'

