from django.urls import re_path  # define URL patterns using regular expressions
from app import consumers  # this handles WebSocket communications

# URLs that handle the WebSocket connection are placed here
websocket_urlpatterns = [
    re_path(
        r"ws/chat/(?P<chat_box_name>\w+)/$",  # use of named capturing group
        consumers.ChatRoomConsumer.as_asgi(),
    ),
]
