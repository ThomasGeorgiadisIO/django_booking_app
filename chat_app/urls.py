from django. urls import path
from .views import *

urlpatterns = [
    path('lobby', lobby, name='lobby'),
    path('room/', room, name="room"),
    path('checkview', checkview, name='checkview'),
    path('send', send, name='send'),
    path('getMessages/<str:room>/', getMessages, name='getMessages'),
]

