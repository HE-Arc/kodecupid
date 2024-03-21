from rest_framework import serializers
from django.contrib.auth import get_user_model

from .tag import TagSerializer
from .picture import PictureSerializer

Tag = get_user_model().tags.through

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )

class UserDetailsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'bio','tags','pfp','looking_for']