from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as authviews
from django.contrib.auth.views import auth_login

from .views import login
from . import views

router = routers.DefaultRouter()

router.register('players',views.PlayerViewSet,basename='player')
router.register('decks', views.DeckViewSet,basename="deck")
router.register('games',views.GameViewSet,basename='game')



urlpatterns = [
    path('', include(router.urls)),
    path('login/',login,name='login'),
    ]
#path('api-token-auth/',authviews.obtain_auth_token,name='api-token-auth'),
    #path('login/',auth_login,name='login'),
    #path('verify/<str:pk>',views.verify),
print(urlpatterns)