from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..serializers import UserSerializer

from ..models import User

import random


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_by_id(request, id):
    if User.objects.filter(id = id).exists():
        user = User.objects.get(id = id)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({"message": "User not found."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def random_user(request):
    users = User.objects.exclude(id=request.user.id)

    # TODO: retreive only the one not liked by the user !

    if len(users) == 0:
        return Response({"message": "Looks like you liked them all"}, status=status.HTTP_404_NOT_FOUND)

    user = random.choice(users)

    serializer = UserSerializer(user, many=False)

    return Response(serializer.data, status=status.HTTP_200_OK)


