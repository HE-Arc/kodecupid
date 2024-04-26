from django.contrib.auth.models import AbstractUser
from django.db import models
from .picture import Picture

class User(AbstractUser):
    # Add additional fields
    bio = models.CharField(max_length=100)
    looking_for = models.CharField(max_length=100)
    tags = models.ManyToManyField('kodecupidapp.Tag', related_name='tags')
    pfp = models.ForeignKey(Picture, related_name='pfp', on_delete=models.CASCADE, null=True, blank=True)
