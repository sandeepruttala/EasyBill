from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from main.consumers import OrderConsumer

websocket_urlpatterns = [
    path('ws/order/', OrderConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('ws/order/', OrderConsumer.as_asgi()),
    ])
})