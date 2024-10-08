# Generated by Django 5.1 on 2024-10-01 19:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0005_post_likes_delete_like'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AddField(
            model_name='topic',
            name='likes',
            field=models.ManyToManyField(related_name='topic_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
