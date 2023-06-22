from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class TodoViewSet(viewsets.ModelViewSet):
    # A viewset for handling CRUD operations on Todo objects.
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    authentication_classes=[BasicAuthentication] # Basic Authentication for authentication
    permission_classes = [IsAuthenticated] # view requires authenticated access

