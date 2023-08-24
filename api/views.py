from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.views import APIView#To override POST GET request function
from rest_framework.response import Response#To create customized response
from .models import Room
from .serializers import RoomSerializer, CreateRoomSerializer



# Create your views here.
# def hello():
#     return HttpResponse("HELLO WORLD")

# class RoomView(generics.CreateAPIView):
#     def get(self, request, format=None):
#         queryset = Room.objects.all()
#         serializer_class = RoomSerializer(queryset,many=True)
#         raise Exception(str(serializer_class.data))
#         return Response(serializer_class.data, status=status.HTTP_200_OK)
class RoomView(APIView):
    def get(self, request, format=None):
        queryset = Room.objects.all()
        serializer_class = RoomSerializer(queryset,many=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)

class CreateRoomView(APIView):
    serializer_class = CreateRoomSerializer
    
    def post(self, request, format=None):

        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
            
        serializer = self.serializer_class(data=request.data)#
        
        if serializer.is_valid():#If data sended from html form have 'can_pause', 'skip_vote'
            guest_can_pause = serializer.data.get('can_pause')
            guest_skip_vote = serializer.data.get('skip_vote')
            host = str(self.request.session.session_key)#Convert session key to string
            query_set =Room.objects.filter(host=host)
            #If same host create room, update data on the current room instead
            if query_set.exists():
                room = query_set[0]#Get this host room data
                room.can_pause = guest_can_pause#update the data
                room.skip_vote = guest_skip_vote#update the data
                room.save(update_fields=['can_pause','skip_vote'])#Save the data
                return Response(RoomSerializer(room).data, status=status.HTTP_200_OK)
            else:
                room = Room(host=host,can_pause=guest_can_pause,skip_vote=guest_skip_vote)
                room.save()
                return Response(RoomSerializer(room).data, status=status.HTTP_201_CREATED)
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)  

'''{
    "can_pause": true,
    "skip_vote": true
}
-) from rest_framework import generics explanation

Dalam Django REST framework, "generics" mengacu pada sekelompok kelas pandangan berbasis kelas yang menyediakan implementasi umum untuk tugas-tugas umum dalam pembangunan API, seperti membuat, membaca, memperbarui, dan menghapus objek dalam basis data.

Kelas-kelas generik ini dirancang untuk mengurangi boilerplate code (kode yang perlu ditulis berulang-ulang) dalam pengembangan API yang umum digunakan. Mereka menyediakan solusi umum untuk operasi CRUD (Create, Read, Update, Delete) dan mempermudah penggunaan pola-pola umum dalam pengembangan RESTful API.

Berikut adalah beberapa kelas generik yang sering digunakan dalam Django REST framework:

ListAPIView: Ini digunakan untuk menampilkan daftar objek dalam basis data. Ini sesuai dengan operasi "READ" dalam operasi CRUD.

CreateAPIView: Ini digunakan untuk membuat objek baru dalam basis data. Ini sesuai dengan operasi "CREATE" dalam operasi CRUD.

RetrieveAPIView: Ini digunakan untuk mengambil objek tunggal dari basis data berdasarkan id atau atribut unik lainnya. Ini sesuai dengan operasi "READ" dalam operasi CRUD.

UpdateAPIView: Ini digunakan untuk memperbarui objek yang ada dalam basis data. Ini sesuai dengan operasi "UPDATE" dalam operasi CRUD.

DestroyAPIView: Ini digunakan untuk menghapus objek dari basis data. Ini sesuai dengan operasi "DELETE" dalam operasi CRUD.

ListCreateAPIView: Menggabungkan fungsionalitas ListAPIView dan CreateAPIView dalam satu pandangan. Ini berguna saat Anda ingin menampilkan daftar objek dan juga mendukung membuat objek baru.

RetrieveUpdateAPIView: Menggabungkan fungsionalitas RetrieveAPIView dan UpdateAPIView dalam satu pandangan. Ini berguna saat Anda ingin mengambil objek tunggal dan juga mendukung pembaruan objek tersebut.

RetrieveUpdateDestroyAPIView: Menggabungkan fungsionalitas RetrieveAPIView, UpdateAPIView, dan DestroyAPIView dalam satu pandangan. Ini berguna saat Anda ingin mengambil, memperbarui, dan menghapus objek dalam satu pandangan.'''

