from django.db import models
from users.models import User
from chat_messages.models import Message
from chats.models import Chat


class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    new_messages = models.IntegerField(default=0)
    last_read_message = models.ForeignKey(Message, on_delete=models.CASCADE)
