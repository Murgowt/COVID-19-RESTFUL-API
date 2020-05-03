from django.shortcuts import render
from django.http import JsonResponse
import datetime
from rest_framework import viewsets
from .models import world
from .serializers import  WorldSerializer
# Create your views here.


class WorldViewSet(viewsets.ModelViewSet):
    queryset=world.objects.all()
    serializer_class = WorldSerializer