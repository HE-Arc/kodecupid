from rest_framework import serializers
from ..models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','bio','looking_for','pfp']

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
    
class UserConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','bio','looking_for','pfp']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def update(self, instance, validated_data):
        instance.username=validated_data.get('username', instance.username)
        instance.set_password(validated_data.get('password', instance.password))
        instance.bio=validated_data.get('bio', instance.bio)
        instance.looking_for=validated_data.get('looking_for', instance.looking_for)
        instance.pfp=validated_data.get('pfp', instance.pfp)

        instance.save()
        return instance
