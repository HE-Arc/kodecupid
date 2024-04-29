from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from ..models import Message, User, Like

class MessageSerializer(serializers.ModelSerializer):
    target_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True )# ,source='target_user')

    class Meta:
        model = Message
        fields = ['id', 'source_user', 'target_user', 'sent', 'content']
        read_only_fields = ['id', 'source_user', 'sent']

    def validate(self, attrs):
        source_user = self.context['request'].user
        target_user = attrs['target_user']

        if not Like.objects.filter(source_user=target_user, target_user=source_user).exists():
            raise ValidationError('Messages can only be sent to users when a match occured.')

        return attrs

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['source_user'] = user
        return Message.objects.create(**validated_data)