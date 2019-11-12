# Generated by Django 2.2.5 on 2019-11-07 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0007_auto_20191107_1458'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attachment',
            options={'verbose_name': 'Прикрепление', 'verbose_name_plural': 'Прикрепления'},
        ),
        migrations.AlterModelOptions(
            name='chat',
            options={'verbose_name': 'Чат', 'verbose_name_plural': 'Чаты'},
        ),
        migrations.AlterModelOptions(
            name='member',
            options={'verbose_name': 'Участник', 'verbose_name_plural': 'Участники'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
        migrations.AlterField(
            model_name='attachment',
            name='chat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.Chat', verbose_name='ID чата'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.Message', verbose_name='ID сообщения'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='type',
            field=models.CharField(max_length=31, verbose_name='Тип прикрепления'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='url',
            field=models.CharField(blank=True, default='', max_length=2090, verbose_name='URL прикрепления'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ID юзера'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='is_group_chat',
            field=models.BooleanField(verbose_name='это групповой чат?'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='last_message',
            field=models.IntegerField(blank=True, null=True, verbose_name='ID последнего сообщения'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='topic',
            field=models.CharField(max_length=16, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='member',
            name='chat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.Chat', verbose_name='ID чата'),
        ),
        migrations.AlterField(
            model_name='member',
            name='last_read_message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chats.Message', verbose_name='ID последнего сообщения'),
        ),
        migrations.AlterField(
            model_name='member',
            name='new_messages',
            field=models.IntegerField(default=0, verbose_name='Количество новых сообщений'),
        ),
        migrations.AlterField(
            model_name='member',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ID юзера'),
        ),
        migrations.AlterField(
            model_name='message',
            name='added_at',
            field=models.DateTimeField(verbose_name='Добавлено'),
        ),
        migrations.AlterField(
            model_name='message',
            name='chat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.Chat', verbose_name='ID чата'),
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.CharField(max_length=4095, verbose_name='Содержание'),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ID юзера'),
        ),
    ]
