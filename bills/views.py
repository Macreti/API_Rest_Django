from django.shortcuts import render
from .models import Personne
from .serializers import PersonneSerializer
from rest_framework import generics

import requests

# Create your views here.

class PersonneListCreate(generics.ListCreateAPIView):
    queryset = Personne.objects.all()
    serializer_class = PersonneSerializer
    

