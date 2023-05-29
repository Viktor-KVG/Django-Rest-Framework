from .models import *
from rest_framework import serializers


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Author
       fields = ['id', 'otch', 'phone']


class CoordinatesSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Coordinates
       fields = ['id', 'latitude', 'longitude', 'height']





class ImagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Images
        fields = ['id','connect_image', 'title', 'file_image',]




class LevelSerializer(serializers.HyperlinkedModelSerializer):
    # image = ImagesSerializer(many=True, read_only=False)
    # coordinates = CoordinatesSerializer(many=True, read_only=False)
    class Meta:
        model = Level
        fields = ['id', 'level_summer', 'level_winter', 'status_positions',
                  'name_obj', 'text', 'coords', 'info_author', 'add_time' ]

    # def create(self, validated_data):
    #     images_data = validated_data.pop('file_image')
    #     level = Level.objects.create(**validated_data)
    #     for image_data in images_data:
    #         Images.objects.create(level=level, **image_data)
    #     return level