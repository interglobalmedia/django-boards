from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from utils.storage_backends import PublicMediaStorage
import pathlib
from django.core.files.storage import default_storage
from io import BytesIO

def _profile_avatar_upload_path(instance, filename):
    """Provides a clean upload path for user avatar images
    """
    file_extension = pathlib.Path(filename).suffix
    return f'profile_images/{instance.id}{file_extension}'

# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(upload_to='_profile_avatar_upload_path', storage=PublicMediaStorage())
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar)

        if img.height > 80 or img.width > 80:
            new_img = (80, 80)
            img.thumbnail(new_img)
            img.save(self.avatar)

        def __str__(self):
            return self.user.username