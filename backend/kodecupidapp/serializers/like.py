from rest_framework import serializers
from ..models import Like, User

class LikeSerializer(serializers.ModelSerializer):
    source_user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True, source='source_user')
    target_user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True, source='target_user')

    # TODO: Change the source user when logging is gonna be handled

    class Meta:
        model = Like
        fields = ['id', 'source_user_id', 'target_user_id', 'created']
        read_only_fields = ['id', 'created']

    def create(self, validated_data):
        return Like.objects.create(**validated_data)