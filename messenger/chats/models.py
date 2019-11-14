from django.db import models
from users.models import User


class Chat(models.Model):
    is_group_chat = models.BooleanField(verbose_name='это групповой чат?')
    topic = models.CharField(max_length=16, verbose_name='Название')
    last_message = models.IntegerField(null=True, blank=True, verbose_name='ID последнего сообщения')  # TODO default = 0
#    last_message = models.ForeignKey('Message', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=4095, verbose_name='Содержание')
    added_at = models.DateTimeField(verbose_name='Добавлено')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Attachment(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    type = models.CharField(max_length=31, verbose_name='Тип прикрепления')
    url = models.CharField(max_length=2090, blank=True, default='', verbose_name='URL прикрепления')

    class Meta:
        verbose_name = 'Прикрепление'
        verbose_name_plural = 'Прикрепления'


class Member(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    new_messages = models.IntegerField(default=0, verbose_name='Количество новых сообщений')
    last_read_message = models.ForeignKey(Message, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'
