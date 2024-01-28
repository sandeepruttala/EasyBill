# main/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class OrderConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        group_name = "order_updates"
        await self.channel_layer.group_add(
            group_name,
            self.channel_name
        )
        # print group
        print(self.channel_layer.groups)

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        if message:
            message = "update"
        group_name = "order_updates"
        await self.channel_layer.group_send(
            group_name,
            {
                'type': 'update_message',
                'message': message
            }
        )

    async def update_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))
