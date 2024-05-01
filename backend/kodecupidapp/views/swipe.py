from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet

from ..serializers import UserSerializer
from ..models import User, Like

import random

class SwipeView(GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'],url_path='<int:pk>')
    def user_by_id(self,request, pk):
        if User.objects.filter(id = pk).exists():
            user = User.objects.get(id = pk)
            serializer = self.serializer_class(user, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "User not found."}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'])  
    def matches(self, request):
        user = request.user
        
        likes_target_user = Like.objects.filter(target_user=user).values_list('source_user', flat=True)
        likes_source_user = Like.objects.filter(source_user=user).values_list('target_user', flat=True)

        mutual_likes_ids = set(likes_target_user).intersection(set(likes_source_user))
        mutual_likes = User.objects.filter(id__in=mutual_likes_ids)

        serializer = self.serializer_class(mutual_likes, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def random_user(self,request):
        users = User.objects.exclude(id=request.user.id)
        cu_user = request.user
        likes_source_user = Like.objects.filter(source_user=request.user).values_list('target_user', flat=True)
        # exclude users that do not have the sex of the user that is looking for
        users = users.exclude(sex=not cu_user.looking_for)
        users = users.exclude(id__in=likes_source_user)


        if len(users) == 0:
            return Response({"message": "Looks like you liked them all"}, status=status.HTTP_404_NOT_FOUND)

        user = random.choice(users)

        serializer = self.serializer_class(user, many=False)

        return Response(serializer.data, status=status.HTTP_200_OK)


