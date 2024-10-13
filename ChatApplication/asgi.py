"""
ASGI config for ChatApplication project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.auth import (
    AuthMiddlewareStack,
)  # Authentication support for WebSocket connections
from channels.routing import (
    ProtocolTypeRouter,
    URLRouter,
)  # route based on the protocol being used and route based on URL patternsfrom channels.auth import AuthMiddlewareStack
from .routing import websocket_urlpatterns

# the default settings module for the 'asgi' program
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ChatApplication.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(
                websocket_urlpatterns,
            ),
        ),
    }
)
