from django.db import models

class Picture(models.Model):
  image = models.ImageField(upload_to='pictures/')
  user = models.ForeignKey('kodecupidapp.User', on_delete=models.CASCADE)