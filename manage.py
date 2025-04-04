#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import django

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

    try:
        from django.core.management import execute_from_command_line
        from django.contrib.auth import get_user_model
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Automatically create superuser if it doesn't exist
    django.setup()
    User = get_user_model()
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@example.com", "adminpassword")
        print("✅ Superuser created: admin / adminpassword")

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
