"""
WSGI config for Django_Demo_WebScrapping project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

#os.environ["DJANGO_SETTINGS_MODULE"] = "Django_Demo_WebScrapping.Django_Demo_WebScrapping.settings"
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_Demo_WebScrapping.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_Demo_WebScrapping.settings_render')

application = get_wsgi_application()
