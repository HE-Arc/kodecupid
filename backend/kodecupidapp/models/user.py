from django.contrib.auth.models import AbstractUser
from django.db import models
from .picture import Picture

class User(AbstractUser):
    # Add additional fields
    bio = models.CharField(max_length=255)
    sex = models.BooleanField()
    looking_for = models.BooleanField()
    tags = models.ManyToManyField('kodecupidapp.Tag', related_name='tags')
    pfp = models.ForeignKey(Picture, related_name='pfp', on_delete=models.SET_NULL, null=True, blank=True)
