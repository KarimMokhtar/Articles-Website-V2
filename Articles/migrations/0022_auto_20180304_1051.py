# Generated by Django 2.0.2 on 2018-03-04 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0021_auto_20180304_1049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user_id',
            new_name='auth_id',
        ),
    ]
