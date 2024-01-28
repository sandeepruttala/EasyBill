# EasyBill/routing.py
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path, re_path
from main.consumers import OrderConsumer

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
            URLRouter(
                [
                    path("ws/orders/", OrderConsumer.as_asgi()),
                    # Add other WebSocket paths if needed
                ]
            )
        ),
})