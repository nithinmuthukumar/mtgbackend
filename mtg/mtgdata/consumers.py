# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from .models import Game
from .serializers import GameSerializer


class ChatConsumer(WebsocketConsumer):
    def connect(self):





        self.accept()
        print(json.dumps(GameSerializer(Game.objects.all(),many=True).data))

        self.send(text_data=json.dumps(GameSerializer(Game.objects.all(),many=True).data))

    def disconnect(self, close_code):
        pass

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        if message['type']=='create':
            GameSerializer.create(message['data'])

