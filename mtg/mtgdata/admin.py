from django.contrib import admin

# Register your models here.
from .models import Player, Card, Deck, Game

admin.site.register(Player)
admin.site.register(Card)
admin.site.register(Deck)

admin.site.register(Game)