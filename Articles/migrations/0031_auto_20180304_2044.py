# Generated by Django 2.0.2 on 2018-03-04 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0030_remove_reply_author_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='user_id',
        ),
    ]