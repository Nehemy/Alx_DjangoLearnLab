from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, blank=True)
    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='customuser_set',
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='customuser_set',
        help_text='Specific permissions for this user.'
    )
