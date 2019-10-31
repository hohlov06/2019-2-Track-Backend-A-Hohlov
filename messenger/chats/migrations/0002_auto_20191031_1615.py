# Generated by Django 2.2.5 on 2019-10-31 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('is_group_chat', models.BooleanField()),
                ('topic', models.CharField(max_length=16)),
            ],
        ),
        migrations.DeleteModel(
            name='Chats',
        ),
    ]
