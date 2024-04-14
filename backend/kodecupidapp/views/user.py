from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from ..models import User
from ..serializers import UserSerializer, UserRegistrationSerializer, UserConfigurationSerializer, TagSerializer

class UserView(APIView):

    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method in ["POST"]:
            return [AllowAny()]
        else:
            return [IsAuthenticated()]

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request):
        serializer = UserConfigurationSerializer(request.user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User configured successfully."}, status=status.HTTP_204_NO_CONTENT)   
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        
        id = request.user.id

        if User.objects.filter(id = id).exists():
            user = User.objects.get(id = id)
            serializer = UserSerializer(user, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response({"message": "User not found."}, status=status.HTTP_404_NOT_FOUND)
    
class UserTagView(APIView):

    def get(self, request):
        user = request.user

        serializer = TagSerializer(user.tags, many=True)

        return Response(serializer.data)