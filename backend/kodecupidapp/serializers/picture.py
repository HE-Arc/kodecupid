from rest_framework import serializers
from ..models import Picture

import base64
import os

class PictureSerializer(serializers.ModelSerializer):

    image_data = serializers.SerializerMethodField()

    class Meta:
        model = Picture
        fields = ['id', 'image', 'image_data', 'user']

    def get_image_data(self, obj):
            if os.path.exists(obj.image.path):
                with open(obj.image.path, 'rb') as image_file:
                    return 'data:image/jpeg;base64,'+ base64.b64encode(image_file.read()).decode()