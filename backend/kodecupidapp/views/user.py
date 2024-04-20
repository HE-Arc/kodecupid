from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import  CreateModelMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.shortcuts import get_object_or_404

from ..models import User, Tag
from ..serializers import UserSerializer, UserRegistrationSerializer, UserConfigurationSerializer, TagSerializer

from rest_framework.decorators import action

class UserView(GenericViewSet, CreateModelMixin):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return UserRegistrationSerializer
        elif self.action == "partial_update":
            return UserConfigurationSerializer
        else:
            return UserSerializer
    
    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        else:
            return [IsAuthenticated()]

    def create(self, request):
        serializer = self.get_serializer_class()(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        user = request.user
        serializer = self.get_serializer_class()(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User configured successfully."}, status=status.HTTP_204_NO_CONTENT)   
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=False, methods=['get'])
    def current(self, request):
        user = request.user
        serializer = self.get_serializer_class()(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['get'])
    def tags(self, request, pk=None):
        user = self.get_object()
        serializer = TagSerializer(user.tags, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def add_tag(self, request):
        serializer = TagSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = request.user

        tag_name = serializer.validated_data['name']
        tag = get_object_or_404(Tag, name=tag_name)

        if tag in user.tags.all():
            return Response({'message': 'User already has tag'}, status=status.HTTP_400_BAD_REQUEST)

        user.tags.add(tag)

        return Response({'message': 'Tag added to user'}, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['delete'])
    def remove_tag(self, request):
        serializer = TagSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = request.user

        tag_name = serializer.validated_data['name']
        tag = get_object_or_404(Tag, name=tag_name)

        if tag not in user.tags.all():
            return Response({'message': 'User does not have tag'}, status=status.HTTP_400_BAD_REQUEST)

        user.tags.remove(tag)

        return Response({'message': 'Tag removed from user'}, status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=False, methods=['post'])
    def add_picture(self, request):
        user = request.user
        user.pfp = request.data['pfp']
        user.save()
        return Response({"message": "Picture added successfully."}, status=status.HTTP_201_CREATED)