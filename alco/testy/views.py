
import django_filters
from rest_framework import viewsets, status
from .serialaizers import *
from .models import *

# Create your views here.

class AuthorViewset(viewsets.ModelViewSet):
   queryset = Author.objects.all()
   serializer_class = AuthorSerializer



class LevelViewset(viewsets.ModelViewSet):
   queryset = Level.objects.all()
   serializer_class = LevelSerializer
   filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
   filterset_fields = ['level_summer', 'level_winter', 'status_positions',
                 'name_obj', 'text', 'coords', 'info_author', 'add_time']


class ImagesViewset(viewsets.ModelViewSet):
   queryset = Images.objects.all()
   serializer_class = ImagesSerializer


class CoordsViewset(viewsets.ModelViewSet):
   queryset = Coordinates.objects.all()
   serializer_class = CoordinatesSerializer





from django.shortcuts import render

# Create your views here.
