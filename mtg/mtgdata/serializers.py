from random import shuffle

from django.contrib.auth.models import User
from django.forms import models
from rest_framework import serializers
from django.db import models
from django.core.mail import send_mail
import string

from .models import Player, Deck, Card, Game


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'



class DeckSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True)
    class Meta:
        model = Deck
        fields = ('owner','name','cards','id')

    def create(self, validated_data):
        cards = validated_data.pop('cards')

        deck = Deck.objects.create(**validated_data)

        for card in cards:
            Card.objects.create(**card)
        return deck

    def update(self, instance, validated_data):

        Card.objects.all().filter(deck=instance).delete()
        for card in validated_data.pop('cards'):
            Card.objects.create(**card)
        instance.save()
        return instance

class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ('username', 'email', 'password','id')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

class GameSerializer(serializers.ModelSerializer):

    players = PlayerSerializer(many=True)

    class Meta:
        model = Game
        fields = ('name','size','format','players')

    # still need to save players to game

    def create(self, validated_data):
        validated_data.pop('players')

        game = Game.objects.create(**validated_data)
        return game





