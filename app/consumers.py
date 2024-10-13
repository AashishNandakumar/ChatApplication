from channels.generic.websocket import (
    AsyncWebsocketConsumer,
)  # helps you create WebSocket Consumers using Async code (i.e, non-blocking code, suitable for handling multiple users or events)
import json


# this class handles the WebSocket lifecycle events like connect, receive, and disconnect
class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_box_name = self.scope["url_route"]["kwargs"]["chat_box_name"]
        self.group_name = f"chat_{self.chat_box_name}"

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name,
        )

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name,
        )

    # this function receives messages from WebSocket
    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]

        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "chatbox_message",
                "message": message,
                "username": username,
            },
        )

    # receive message from room group
    async def chatbox_message(self, event):
        message = event["message"]
        username = event["username"]
        # send message and username of sender to websocket
        await self.send(
            text_data=json.dumps(
                {
                    "message": message,
                    "username": username,
                }
            )
        )

    # pass
