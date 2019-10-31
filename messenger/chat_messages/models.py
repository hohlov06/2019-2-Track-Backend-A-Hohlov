from django.db import models
from chats.models import Chat
from users.models import User


class Message(models.Model):
    id = models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=4095)
    added_at = models.DateTimeField()
