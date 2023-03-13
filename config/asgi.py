"""
ASGI config for portfolyoFaruk project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.product')
CSRF_TRUSTED_ORIGINS = ['https://*.up.railway.app','https://*.127.0.0.1:8000','https://data-tagger-production.up.railway.app']

application = get_asgi_application()
