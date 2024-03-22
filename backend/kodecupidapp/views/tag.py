from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from ..models import Tag
from ..serializers import TagSerializer
from ..models import User


class TagView(APIView):

    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
    
    def post(self, request):

        tag_id = request.data.get('tag_id')

        user = request.user

        tag = get_object_or_404(Tag, id=tag_id)

        if user in tag.users.all():
            return Response({'message': 'User already has tag'}, status=status.HTTP_400_BAD_REQUEST)
        
        tag.users.add(user)

        return Response({'message': 'Tag added to user'}, status=status.HTTP_201_CREATED)
