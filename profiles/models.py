from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    User profile model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(
        upload_to='media/profile_images', default='profile_images/default')

    def __str__(self):
        return self.user.username
