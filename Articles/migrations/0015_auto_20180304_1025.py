# Generated by Django 2.0.2 on 2018-03-04 08:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0014_remove_post_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
