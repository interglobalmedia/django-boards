from settings.base import *
# you need to set "myproject = 'prod'" as an environment variable
# in your OS (on which your website is hosted)
if os.environ['DJANGO_BOARDS'] == 'prod':
   from settings.prod import *
else:
   from settings.dev import *