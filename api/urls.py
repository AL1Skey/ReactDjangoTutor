from .views import *
from django.urls import path, include

urlpatterns = [
    # path('hidden',hello,name='hidden'),
    path('api/room',RoomView.as_view()),
    path('api/create-room',CreateRoomView.as_view())
]

