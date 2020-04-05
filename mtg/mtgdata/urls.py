from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as authviews
from django.contrib.auth.views import auth_login

from .views import login, sample_api
from . import views

router = routers.DefaultRouter()

router.register('players',views.PlayerViewSet,basename='player')
router.register('decks', views.DeckViewSet,basename="deck")


urlpatterns = [
    path('', include(router.urls)),
    path('login/',login,name='login'),
    path('sampleapi/', sample_api)
    ]
#path('api-token-auth/',authviews.obtain_auth_token,name='api-token-auth'),
    #path('login/',auth_login,name='login'),
    #path('verify/<str:pk>',views.verify),
print(urlpatterns)