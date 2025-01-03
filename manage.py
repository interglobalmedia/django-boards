#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)
from django_boards.settings import development, production
import sys

def main():
    """Run administrative tasks."""
    # in order for development env to work, must be set to development here locally. Must be set to production before deploying to Render. The "if elif" condition takes care of that.
    DEVELOPMENT_ENVIRONMENT = os.getenv("ENVIRONMENT")
    PRODUCTION_ENVIRONMENT = os.environ.get("ENVIRONMENT")
    if development:
        print(development, 'in development')
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DEVELOPMENT_ENVIRONMENT")
    elif production:
        print(production, 'in production')
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PRODUCTION_ENVIRONMENT")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
