from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_cascade=models.CASCADE)
    photo = models.ImageField(default='user/photos/default.png', upload_to='profile_pics')