from .base import *
# you need to set "myproject = 'prod'" as an environment variable
# in your OS (on which your website is hosted)
PROD = os.environ.get('PROD')
if PROD == True:
   from .prod import *
else:
   from .dev import *