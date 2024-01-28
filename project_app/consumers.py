import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ProjectConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        pass
        # Implement WebSocket connection logic here

    async def disconnect(self, close_code):
        pass
        # Implement WebSocket disconnection logic here

    async def receive(self, text_data):
        pass
        # Implement WebSocket data receiving and broadcasting here
    
    async def send_project_update(self, event):
        message = event['message']

        # Send the project update to the WebSocket client
        await self.send(text_data=json.dumps({'message': message}))

    async def send_task_update(self, event):
        message = event['message']

        # Send the task update to the WebSocket client
        await self.send(text_data=json.dumps({'message': message}))
