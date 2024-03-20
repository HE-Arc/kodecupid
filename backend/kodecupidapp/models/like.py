from django.db import models
from .user import User

class Like(models.Model):
    # Add additional fields
    source_user = models.ForeignKey(User, related_name='source_user', on_delete=models.CASCADE)
    target_user = models.ForeignKey(User, related_name='target_user', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['source_user', 'target_user'], name='unique_like')
        ]