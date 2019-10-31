from django.db import models
from chats.models import Chat
from users.models import User
from chat_messages.models import Message


class Attachment(models.Model):
    id = models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    type = models.CharField(max_length=31)
    url = models.CharField(max_length=2090, blank=True, default='')
