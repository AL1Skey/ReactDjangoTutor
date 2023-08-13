# Set up
- ### Install the necessary tools
```bat
pip install virtualenvwrapper-win django djangorestframework
```
- ### Create backend and front-end app
```
django-admin startapp api
django-admin startapp frontend
```
- ### Insert backend as api on settings.py
```py
......
INSTALLED_APPS = [
    ....,
    'api.apps.ApiConfig',
    ....
]
.....
```

# BackEnd (./api)
-   Make the models and the backend logic
```py
from django.db import models
import random
import string #for ASCII

def generate_code():#Generate Unique ASCII code
    length=7
    
    while True:
        code = ''.join(random.choices(string.ascii_uppercase(),k=length))
        if Room.objects.filter(code=code).count == 0:
            break
    return code

# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length=8,default="",unique=True)
    host = models.CharField(max_length=8,unique=True)
    can_pause = models.BooleanField(null=False, default=False)
    skip_vote = models.IntegerField(null=False, default=1)
    create_at = models.DateTimeField(auto_now_add=True)
```

- ### Create serializers.py to parse ORM to json format on frontend latter
```py
from rest_framework import serializers  #Get serializer function
from .models import Room    #Get model

class RoomSerializer(serializers.Serializer):#Create serializer
    class Meta:#Configure the serializers function
        model = Room #Add room as models
        fields = ('id', 'code', 'host', 'can_pause', 'skip_vote','create_at')#Create tuples of table column based on Models you created
```

- ### Go to views.py and create the Route function to run serializer with generics method from rest_framework and show it as api data
```py
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Room
from .serializers import RoomSerializer

class RoomView(generics.CreateAPIView):#Crea
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
.....
```

- ### Go to urls.py and add the connection to class inside views as views
```py
from .views import *
from django.urls import path, include

urlpatterns = [
    # path('hidden',hello,name='hidden'),
    path('room',RoomView.as_view())
]
```

# FrontEnd
- ## Setup
    -  Go to fronted directory and create static,src and templates
    -  Inside static, create bundle(to store node package), css and images
    -  Inside src, create components(to store React Component)
    - Initialize node.js
    ```cmd
    npm init -y
    ```
    - Install webpack(to bundle the package into one)and webpack-cli
    ```cmd
    npm install webpack webpack-cli --save-dev
    ```
    - Install babel(to make js compatible in any browser by converting the language to compatible language (ex:ES6 to ES5))