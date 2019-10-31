from django.db import models


class Chat(models.Model):
    id = models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')
    is_group_chat = models.BooleanField()
    topic = models.CharField(max_length=16)
