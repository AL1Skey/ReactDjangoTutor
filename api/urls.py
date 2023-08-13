from .views import *
from django.urls import path, include

urlpatterns = [
    # path('hidden',hello,name='hidden'),
    path('room',RoomView.as_view())
]

