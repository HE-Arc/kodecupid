from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ..models import Picture
from ..serializers import PictureSerializer


class PictureView(GenericViewSet, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):

        modified_data = request.data.copy()
        modified_data['user'] = request.user.id

        serializer = self.get_serializer(data=modified_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Picture added successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request):
        instance = self.get_object()
        if request.user.id == instance.user.id:
            self.perform_destroy(instance)
            return Response({"message": "Picture successfully deleted."}, status=status.HTTP_204_NO_CONTENT)
        return Response({"message": "Picture cannot be deleted by another user."}, status=status.HTTP_403_FORBIDDEN)
