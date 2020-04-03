from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Player(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    num_games = models.IntegerField(default=0)


class Deck(models.Model):
    name = models.CharField(max_length=30)

    owner = models.ForeignKey(Player,on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']



class Card(models.Model):
    name = models.CharField(max_length=200)
    version = models.CharField(max_length=15)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE,related_name="cards",default=None)
















