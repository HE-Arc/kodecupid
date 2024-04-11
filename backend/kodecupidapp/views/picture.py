from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ..models import Picture
from ..serializers import PictureSerializer

import random

class PictureView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        modified_data = request.data.copy()
        modified_data['user'] = request.user.id

        serializer = PictureSerializer(data=modified_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Picture added successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        id = request.user.id
        if Picture.objects.filter(id = id).exists():
            pic = Picture.objects.get(id = id)
            serializer = PictureSerializer(pic, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Picture not found."}, status=status.HTTP_404_NOT_FOUND)
            
    def delete(self, request):
        id = int(request.data["id"])
        if Picture.objects.filter(id = id).exists():
            pic = Picture.objects.get(id = id)
            if request.user.id == pic.user.id:
                pic.delete()
                return Response({"message": "Picture successfully deleted."},status=status.HTTP_204_NO_CONTENT)
            return Response({"message": "Picture cannot be deleted by another user."}, status=status.HTTP_403_FORBIDDEN)
        return Response({"message": "Picture not found."}, status=status.HTTP_404_NOT_FOUND)
    