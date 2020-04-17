from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.

class PlayerManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError("must have an email")
        if not username:
            raise ValueError("must have a username")
        user = self.model(
            email = self.normalize_email(email),
            username = username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,username,password=None):
        if not email:
            raise ValueError("must have an email")
        if not username:
            raise ValueError("must have a username")
        user = self.model(
            email = self.normalize_email(email),
            username = username
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.set_password(password)
        user.save(using=self._db)
        return user
class Game(models.Model):
    name = models.CharField(max_length=30)
    size = models.IntegerField()
    format = models.CharField(max_length=40,choices=[("1","Standard"),("2","Modern"),("3","EDH")])

class Player(AbstractBaseUser):
    objects=PlayerManager()
    email = models.EmailField(verbose_name='email',max_length=60,unique=True)

    username = models.CharField(max_length=100,unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined',auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login',auto_now_add=True)
    password = models.CharField(max_length=20)
    num_games = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    wins = models.IntegerField(default=0)
    loss = models.IntegerField(default=0)
    game = models.ForeignKey(Game,on_delete=models.CASCADE,blank=True,null=True,related_name='players')
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS = ['username']

    def has_perm(self,perm,obj=None):
        return self.is_admin
    def has_module_perms(self,app_label):
        return True



class Deck(models.Model):
    name = models.CharField(max_length=30)

    owner = models.ForeignKey(Player,on_delete=models.CASCADE)
    public = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']



class Card(models.Model):
    name = models.CharField(max_length=200)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE,related_name="cards",default=None)
















