from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from ..models import User
from ..serializers import UserSerializer, UserRegistrationSerializer, UserConfigurationSerializer

import random

class UserView(APIView):

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
        if "id" in request.query_params:
            id = request.query_params["id"]

            if id == "random":
                try:
                    users = User.objects.all()
                    user = random.choice(users)
                    # while loop not safe if only 1 user (infinite loop)
                    while user.id == request.user.id:
                        user = random.choice(users) 
                    serializer = UserSerializer(user, many=False)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except:
                    return Response({"message": "No random user could be found."}, status=status.HTTP_404_NOT_FOUND)

            else:
                if User.objects.filter(id = id).exists():
                    user = User.objects.get(id = id)
                    serializer = UserSerializer(user, many=False)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            id = request.user.id
            if User.objects.filter(id = id).exists():
                user = User.objects.get(id = id)
                serializer = UserSerializer(user, many=False)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"message": "User not found."}, status=status.HTTP_404_NOT_FOUND)

            
    def delete(self, request):
        id = int(request.data["id"])
        if User.objects.filter(id = id).exists():
            if id == request.user.id:
                user = User.objects.get(id = id)
                user.delete()
                return Response({"message": "User successfully deleted."},status=status.HTTP_204_NO_CONTENT)
            return Response({"message": "User cannot be deleted."}, status=status.HTTP_403_FORBIDDEN)
        return Response({"message": "User not found."}, status=status.HTTP_404_NOT_FOUND)