from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Room
from .serializers import RoomSerializer

# Create your views here.
# def hello():
#     return HttpResponse("HELLO WORLD")

class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

'''
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