"""
ASGI config for django_boards project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_boards.settings.production')

from django.core.asgi import get_asgi_application

application = get_asgi_application()
