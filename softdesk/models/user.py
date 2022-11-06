from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.functions import Lower


class User(AbstractUser):
    """Extend django auth user class."""

    def __str__(self):
        return self.get_full_name().strip() or self.username

    class Meta:
        app_label = 'softdesk'
        swappable = "AUTH_USER_MODEL"
        constraints = [
            models.UniqueConstraint(Lower('email'), name='unique_email')
        ]

