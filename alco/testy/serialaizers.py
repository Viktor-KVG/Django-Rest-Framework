from .models import *
from rest_framework import serializers


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Author
       fields = ['id', 'username','first_name', 'last_name', 'otch', 'email', 'phone']


class CoordinatesSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Coordinates
       fields = ['id', 'latitude', 'longitude', 'height']





class ImagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Images
        fields = ['id','connect_image', 'title', 'file_image',]




class LevelSerializer(serializers.HyperlinkedModelSerializer):
    # info_author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # image = ImagesSerializer(many=True, read_only=False)
    # coordinates = CoordinatesSerializer(many=True, read_only=False)
    class Meta:
        model = Level
        fields = ['id', 'level_summer', 'level_winter', 'status_positions',
                  'name_obj', 'text', 'coords', 'info_author', 'add_time', ] #'image', 'coordinates'

    # def update(self, instance, validated_data):
    #     instance.level_summer = validated_data.get('level_summer', instance.level_summer)
    #     instance.level_winter = validated_data.get('level_winter', instance.level_winter)
    #     return instance