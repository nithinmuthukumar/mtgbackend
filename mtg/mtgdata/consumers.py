# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from .models import Game, Player
from .serializers import GameSerializer

from rest_framework.authtoken.models import Token
class LobbyConsumer(WebsocketConsumer):

    def connect(self):
        headers = dict(self.scope['headers'])
        if b'authorization' in headers:
            try:
                token_name, token_key = headers[b'authorization'].decode().split()
                if token_name == 'Token':
                    token = Token.objects.get(key=token_key)
                    self.scope['user'] = token.user
                    self.accept()
                    self.update()
            except Token.DoesNotExist:
                print(Token.DoesNotExist)
                return



    def disconnect(self, close_code):
        pass

    # Receive message from WebSocket
    def receive(self, text_data):
        message = json.loads(text_data)
        data = message['data']
        if message['type']=='create':

            game = GameSerializer(data=data)


            if game.is_valid():
                game.save()
                self.scope['user'].game = game.validated_data
                self.scope['user'].save()
                self.update()
            else:

                print(game.errors)

    def update(self):
        self.send(text_data=json.dumps(GameSerializer(Game.objects.all(), many=True).data))




