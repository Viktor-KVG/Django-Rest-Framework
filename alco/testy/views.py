
import django_filters
from django.http import HttpResponse
from rest_framework import viewsets, status, generics, mixins
from rest_framework.decorators import action, api_view
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response

from .serialaizers import *
from .models import *

# Create your views here.

class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # permission_classes = (IsAdminUser, )



class LevelViewset(viewsets.ModelViewSet):
    queryset = Level.objects.all()

    serializer_class = LevelSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['status_positions', 'name_obj', 'text', 'coords',]
    permission_classes = (IsAuthenticatedOrReadOnly,)

    @api_view(['GET'])
    def get_data(request, pk):
        try:
            level = Level.objects.get(pk=pk)
        except level.DoesNotExist:
            return Response(status=404)
        serializer = LevelSerializer(level)
        return Response(serializer.data)


    @api_view(['PATCH'])
    def level_view(request, pk):
        levels = Level.objects.get(pk=pk)
        if levels != 'NE':
            return Response({'state':0, 'message': 'не допустимо для редактирования'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = LevelSerializer(levels, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'state':1, 'message': 'успешно'},status=status.HTTP_200_OK)
        return Response({'state':0, 'message': 'ошибка'}, status= status.HTTP_400_BAD_REQUEST)



















   # @action(detail=True, methods=['get'])
   # def status(self, request, pk=None):
   #    lev = Level.objects.get(pk=pk)
   #
   #       return Response({'status':lev.status_positions})


          # @action(detail=False, methods=['get'])
          # def all_status(self, request, ):
          #    lev = Level.objects.all()
          #    return Response({'lev':lev})



# def put(self, request, *args, **kwargs):
   #    return self.update(request, *args, **kwargs)
   #
   # def putch(self,request, *args, **kwargs):
   #    return self.partial_update(request, *args, **kwargs)


class ImagesViewset(viewsets.ModelViewSet):
   queryset = Images.objects.all()
   serializer_class = ImagesSerializer


class CoordsViewset(viewsets.ModelViewSet):
   queryset = Coordinates.objects.all()
   serializer_class = CoordinatesSerializer


class UpdateViewset(generics.UpdateAPIView):
   queryset = Level.objects.all()
   serializer_class = LevelSerializer

   # def put(self, request, *args, **kwargs):
   #     return self.update(request, *args, **kwargs)
   #
   # def putch(self,request, *args, **kwargs):
   #     return self.partial_update(request, *args, **kwargs)
   #








from django.shortcuts import render

# Create your views here.
