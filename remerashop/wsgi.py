"""
WSGI config for remerashop project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""
# +++++++++++ DJANGO +++++++++++
import os
import sys

# le indicamos el path del project
path = '/home/remerashop/remerasshop'
if path not in sys.path:
    sys.path.append(path)

from django.core.wsgi import get_wsgi_application
# le indicamos el lugar de los settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'remerashop.settings')
application = get_wsgi_application()