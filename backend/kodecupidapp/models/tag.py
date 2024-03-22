from django.db import models

class Tag(models.Model):
  name = models.CharField(max_length=100)
  users = models.ManyToManyField('kodecupidapp.User', related_name='tags')
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)