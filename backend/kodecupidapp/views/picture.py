from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ..models import Picture
from ..serializers import PictureSerializer

from django.http import HttpResponse

import os

class PictureView(GenericViewSet, CreateModelMixin, RetrieveModelMixin, ListModelMixin, DestroyModelMixin):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        modified_data = request.data.copy()
        modified_data['user'] = request.user.id

        serializer = self.get_serializer(data=modified_data)
        if serializer.is_valid():
            instance = serializer.save()
            # Access the ID of the newly created instance
            new_id = instance.id
            return Response({"message": "Picture added successfully.", "id": new_id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        user = request.user

        if user.pfp:
            queryset = Picture.objects.filter(user=user).exclude(id=user.pfp.id)
            serializer = self.get_serializer(queryset, many=True)

        else:
            return Response({"message": "User does not have a profile picture."}, status=status.HTTP_404_NOT_FOUND)
        

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        if pk == '-1':
            instance = self.get_queryset().last()
        else :
            instance = self.get_object()
        
        # Get the image path
        image_path = instance.image.path
        # Read the image data
        image_data = None
        if os.path.exists(image_path):
            with open(image_path, 'rb') as image_file:
                image_data = image_file.read()

        # Return the image data in an HTTP response
        response = HttpResponse(image_data, content_type='image/jpeg')
        response['Content-Disposition'] = 'attachment; filename="image.jpg"'
        return response

    def destroy(self, request, pk=None):
        instance = self.get_object()
        if os.path.exists(instance.image.path):
            os.remove(instance.image.path)
        Picture.objects.filter(id=pk).delete()

        return Response({"message": "Picture deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
