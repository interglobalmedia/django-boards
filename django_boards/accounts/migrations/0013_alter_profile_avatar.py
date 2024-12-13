# Generated by Django 5.1.3 on 2024-12-13 14:22

import accounts.models
import utils.storage_backends
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='default.jpg', null=True, storage=utils.storage_backends.PublicMediaStorage(), upload_to=accounts.models._profile_avatar_upload_path),
        ),
    ]
