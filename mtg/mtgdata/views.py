from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.decorators import api_view, action, permission_classes
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
from rest_framework.authtoken.models import Token

from .models import Player, Deck, Game
from .serializers import PlayerSerializer, DeckSerializer, GameSerializer
from . import serializers
from . import models


class PlayerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
class GameViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Game.objects.all()
    serializer_class = GameSerializer



class DeckViewSet(viewsets.ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        request.data['owner']=request.user.id
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        request.data['owner']=request.user.id
        return super().update(request, *args, **kwargs)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    print(request.data)

    email = request.data.get("email")
    password = request.data.get("password")
    if email is None or password is None:
        return Response({'error': 'Please provide both email and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(email=email, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    print(PlayerSerializer(user).data)
    return Response({'token': token.key,
                     'user':PlayerSerializer(user).data,'decks':DeckSerializer(Deck.objects.all().filter(owner=user),many=True).data},
                    status=HTTP_200_OK)












