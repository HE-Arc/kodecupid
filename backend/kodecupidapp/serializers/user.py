from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'bio', 'looking_for', 'pfp']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_password(self, value):
        return make_password(value)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            bio=validated_data['bio'],
            looking_for=validated_data['looking_for'],
            password=validated_data['password'],  # Password is already hashed from the validate_password method
            pfp=validated_data.get('pfp')  # Assuming 'pfp' is correctly handled if provided
        )
        return user