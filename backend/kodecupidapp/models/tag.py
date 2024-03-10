from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
  name = models.CharField(max_length=100)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)