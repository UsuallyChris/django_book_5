""" Model definitions for users app """
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """ Custom User definition """
    age = models.PositiveIntegerField(null=True, blank=True)
