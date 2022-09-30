"""
ASGI config for shuroop project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
import devices.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shuroop.dev')

django_asgi_app = get_asgi_application()
application = ProtocolTypeRouter({
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                devices.routing.websocket_urlpatterns
            )
        )
    ),
})
