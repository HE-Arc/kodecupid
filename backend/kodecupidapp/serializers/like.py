from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from ..models import Like, User

class LikeSerializer(serializers.ModelSerializer):
    target_user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True, source='target_user')

    class Meta:
        model = Like
        fields = ['id', 'target_user_id', 'created']
        read_only_fields = ['id', 'created']

    def validate(self, attrs):
        user = self.context['request'].user
        target_user = attrs['target_user']

        if(user == target_user):
            raise ValidationError("You sure you like yourself this much? Liking yourself isn't allowed here.")

        if Like.objects.filter(source_user=user, target_user=target_user).exists():
            raise ValidationError('You have already liked this user.')

        return attrs


    def create(self, validated_data):
        user = self.context['request'].user.id
        validated_data['source_user_id'] = user
        return Like.objects.create(**validated_data)