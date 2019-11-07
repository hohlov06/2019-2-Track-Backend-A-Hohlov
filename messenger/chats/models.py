from django.db import models
from users.models import User


class Chat(models.Model):
    is_group_chat = models.BooleanField()
    topic = models.CharField(max_length=16)
    last_message = models.IntegerField(null=True, blank=True)
#    last_message = models.ForeignKey('Message', on_delete=models.CASCADE, null=True)


class ChatUser(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Message(ChatUser):
    # chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=4095)
    added_at = models.DateTimeField()


class Attachment(ChatUser):
    # chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    type = models.CharField(max_length=31)
    url = models.CharField(max_length=2090, blank=True, default='')


class Member(ChatUser):
    # chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    new_messages = models.IntegerField(default=0)
    last_read_message = models.ForeignKey(Message, on_delete=models.CASCADE, null=True, blank=True)
