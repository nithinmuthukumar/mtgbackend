from random import shuffle

from django.contrib.auth.models import User
from django.forms import models
from rest_framework import serializers
from django.db import models
from django.core.mail import send_mail
import string

from .models import Player, Deck, Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class DeckSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True)

    class Meta:
        model = Deck
        fields = '__all__'

    def create(self, validated_data):
        cards = validated_data.pop('cards')

        #validated_data.add(Player.objects.all().filter(username=validated_data.pop('username'))[0].id)
        deck = Deck.objects.create(**validated_data)

        for card in cards:
            Card.objects.create(deck=deck, **card)
        return deck

class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
