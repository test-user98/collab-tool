from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from project_app import consumers

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/some_path/", consumers.ProjectConsumer.as_asgi()),
    ]),
})
