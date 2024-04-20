from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ..models import Picture
from ..serializers import PictureSerializer

from django.http import HttpResponse

import os


class PictureView(GenericViewSet, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin):
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

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # serializer = self.get_serializer(instance)
        
        # Get the image path
        image_path = instance.image.path
        # Read the image data
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()

        # Return the image data in an HTTP response
        response = HttpResponse(image_data, content_type='image/jpeg')
        response['Content-Disposition'] = 'attachment; filename="image.jpg"'
        return response

    # def retrieve(self, request, pk=None):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)

    #     # content_type = "image/png"  # Adjust according to the actual image type

    # # Return the picture data in an HTTP response
    # # return HttpResponse(picture_data, content_type=content_type)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request):
        instance = self.get_object()
        if request.user.id == instance.user.id:
            self.perform_destroy(instance)
            return Response({"message": "Picture successfully deleted."}, status=status.HTTP_204_NO_CONTENT)
        return Response({"message": "Picture cannot be deleted by another user."}, status=status.HTTP_403_FORBIDDEN)
