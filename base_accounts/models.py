from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .managers import BaseUserManager

class BaseUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = BaseUserManager()

    class Meta:
        abstract = True

    def __str__(self):
        return self.email
