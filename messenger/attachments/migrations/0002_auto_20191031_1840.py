# Generated by Django 2.2.5 on 2019-10-31 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attachments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='url',
            field=models.CharField(blank=True, default='', max_length=2090),
        ),
    ]
