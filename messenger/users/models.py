from django.db import models


class User(models.Model):
    name = models.CharField(max_length=63)
    nick = models.CharField(max_length=31, blank=True, default='')
    avatar = models.CharField(max_length=2090, blank=True, default='')
