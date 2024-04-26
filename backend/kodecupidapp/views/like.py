from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers import LikeSerializer
from ..models import Like

class LikeView(APIView):

    def post(self, request):
        serializer = LikeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            like_instance = serializer.save()

            source_user = request.user
            target_user = like_instance.target_user

            match_exists = Like.objects.filter(source_user=target_user, target_user=source_user).exists()

            
            response_data = serializer.data
            response_data['match'] = match_exists

            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
