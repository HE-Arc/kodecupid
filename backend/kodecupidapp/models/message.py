from django.db import models
from .user import User

class Message(models.Model):
    source_user = models.ForeignKey(User, related_name='message_source_user', on_delete=models.CASCADE)
    target_user = models.ForeignKey(User, related_name='message_target_user', on_delete=models.CASCADE)
    sent = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=255)