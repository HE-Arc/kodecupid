from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from ..serializers import MessageSerializer
from ..models import Message

class MessageView(GenericViewSet, CreateModelMixin, ListModelMixin):
    queryset = Message.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = MessageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            response_data = serializer.data
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request, *args, **kwargs):
        target_user = request.query_params.get('target_user')
        if target_user is not None:
            message_list = Message.objects.filter(source_user=request.user, target_user=target_user).values() | Message.objects.filter(source_user=target_user, target_user=request.user).values()
            serializer = self.get_serializer(message_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Messages can only be retrieved for a conversation, try adding target_user as a request parameter"}, status=status.HTTP_400_BAD_REQUEST)