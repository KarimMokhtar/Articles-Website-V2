# Generated by Django 2.0.2 on 2018-03-04 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0012_auto_20180304_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
    ]