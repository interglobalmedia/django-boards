from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from utils.storage_backends import PublicMediaStorage
import pathlib
from django.core.files.storage import default_storage
from io import BytesIO
import os

# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images', storage=PublicMediaStorage())
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        memfile = BytesIO()

        img = Image.open(self.avatar)

        if img.height > 80 or img.width > 80:
            new_img = (80, 80)
            img.thumbnail(new_img, Image.ANTIALIAS)
            img.save(memfile, 'JPEG', quality=95)
            default_storage.save(self.avatar.name, memfile)
            memfile.close()
            img.close()

        def __str__(self):
            return self.user.username