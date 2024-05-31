from re import I
from django.shortcuts import render
from .models import BookModel
from .serializers import BookSerializer,UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import viewsets



class BookDetail(viewsets.ModelViewSet):
    queryset=BookModel.objects.all()
    serializer_class=BookSerializer
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthenticated,]

class UserDetail(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
