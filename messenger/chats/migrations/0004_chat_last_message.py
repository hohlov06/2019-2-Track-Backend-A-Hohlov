# Generated by Django 2.2.5 on 2019-11-06 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0003_auto_20191106_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='last_message',
            field=models.IntegerField(null=True),
        ),
    ]
