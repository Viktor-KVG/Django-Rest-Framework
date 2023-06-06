
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
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['email']
    # permission_classes = (IsAdminUser, )




class LevelViewset(viewsets.ModelViewSet):
    queryset = Level.objects.all()

    serializer_class = LevelSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['status_positions', 'name_obj', 'text', 'coords', 'info_author']
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


    @action(detail=False)
    def show_information(self, request):
        show_information = Level.objects.all().filter(info_author = 2 )
        author = Level.info_author
        page = self.paginate_queryset(show_information)
        if page is author:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(show_information, many=True)
        return Response(serializer.data)




class ImagesViewset(viewsets.ModelViewSet):
   queryset = Images.objects.all()
   serializer_class = ImagesSerializer


class CoordsViewset(viewsets.ModelViewSet):
   queryset = Coordinates.objects.all()
   serializer_class = CoordinatesSerializer


class UpdateViewset(generics.UpdateAPIView):
   queryset = Level.objects.all()
   serializer_class = LevelSerializer





# Create your views here.
