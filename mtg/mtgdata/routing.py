# chat/urls.py
from django.urls import path

from . import views

from django.urls import re_path

from . import consumers
# mysite/routing.py
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
websocket_urlpatterns = [
    re_path(r'ws/lobby/', consumers.ChatConsumer),
]

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),

})