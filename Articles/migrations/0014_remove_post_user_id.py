# Generated by Django 2.0.2 on 2018-03-04 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0013_auto_20180304_1023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user_id',
        ),
    ]
