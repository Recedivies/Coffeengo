from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from users.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        verbose_name="Username",
        max_length=16,
        unique=True,
        validators=[MinLengthValidator(1)],
    )

    email = models.EmailField(_("Email Address"), unique=True)

    password = models.CharField(_("password"), max_length=255)

    is_staff = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email} - {self.username}"
