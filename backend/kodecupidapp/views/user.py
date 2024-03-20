from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from ..serializers import UserRegistrationSerializer, UserConfigurationSerializer

class UserView(APIView):

    def get_permission_classes(self):
        if self.request.method in ["POST"]:
            return [AllowAny]
        else:
            return [IsAuthenticated]

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request):
        serializer = UserConfigurationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User configured successfully."}, status=status.HTTP_204_NO_CONTENT)   
