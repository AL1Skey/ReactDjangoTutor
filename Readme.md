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
    -  Go to frontend directory and create static,src and templates
    -  Add frontend.api.FrontendConfig inside installed app on settings.py
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
    ```cmd
    npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev
    npm i @babel/plugin-proposal-class-properties 
    ```
    - Install React
    ```cmd
    npm i react react-dom -save-dev react-router-dom
    ```
    - (optional) Install material-ui
    ```cmd
    npm install @mui/material @mui/styled-engine-sc styled-components
    npm install @mui/icons-material
    ```
    - Create babel.config.json in frontend folder and write this
    ```json
    {
    "presets": [
        [
            "@babel-presets-env",{
                "target":{
                    "node":10
                }
            }
        ]
    ],
    "plugins": [
        "@babel/plugin-proposal-class-properties"
    ]   
    }
    ```
    - Create webpack.config.js and use this code as configuration
    ```js
    const path = require("path");
    const webpack = require("webpack");

    module.exports = {
    entry: "./src/index.js",
    output: {
        path: path.resolve(__dirname, "./static/bundle"),
        filename: "[name].js",
    },
    module: {
        rules: [
        {
            test: /\.js$/,
            exclude: /node_modules/,
            use: {
            loader: "babel-loader",
            },
        },
        ],
    },
    optimization: {
        minimize: true,
    },
    plugins: [
        new webpack.DefinePlugin({
        "process.env": {
            // This has effect on the react lib size
            NODE_ENV: JSON.stringify("production"),
        },
        }),
    ],
    };
    ```
    - Create index.js inside src as entry-point
    - Add this on package.json as shortcut to run webpack with npm
    ```json
    .....
    "scripts": {
    "dev": "webpack --mode development --watch",
    "build": "webpack --mode production"
    },
    .....
    ```
    - Add html file inside frontend/templates/frontend as entry point for entry point on index.js and add this code
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        {% load static %}
        <script src="https://code.jquery.com/jquery-3.7.0.min.js" integrity="sha256-2Pmvv0kuTBOenSvLm6bvfBSSHrUJ+3A7x6P5Ebd07/g=" crossorigin="anonymous"></script>
        <script src="https://code.jquery.com/jquery-2.2.4.min.js" integrity="sha256-BbhdlvQf/xTY9gja0Dq3HiwQF8LaCRTXxZKRutelT44=" crossorigin="anonymous"></script>
        <link rel="stylesheet" type="text/css" href="{% static 'css/index.css'%}" >
        <title>React Django Project</title>
    </head>
    <body>
        <div id="main">
            <div id="app">
                
            </div>
        </div>
        <script src="{% static 'bundle/main.js' %}"></script>
    </body>
    </html>
    ```
    - Add this funtion on frontend/views.py
    ```py
    from django.shortcuts import render

    # Create your views here.
    def index(request, *args, **kwargs):
        return render(request,'frontend/index.html')
    ```
    - Route the views function to urls and route the frontend urls to main project urls
    - Create basic react view as testing water with this code below
    ```js
    import React, {Component} from "react";
    import { render } from "react-dom";

    export default class App extends Component {//Export this class as default and inherit Component class
        constructor(props){//Make constructor
            super(props);
        }

        render(){// Render the html code
            return (
                <div>
                    <h1>Hello World!</h1>
                </div>
            );
        }
    }

    render(<App />, document.getElementById("app"));// Link the react output to html tag with id of app
    ```
    - Add this code inside frontend/src/index.js to initialize react which is to be compressed and transpiloting by babel
    ```js
    import App from "./components/App";
    ```
    - Run webpack in watch mode with shortcut command according to script inside package.json
    ```cmd
    npm run dev        
    ```