from django.db import models
from users.managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils import timezone


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        verbose_name="Username",
        max_length=8,
        unique=True,
        validators=[MinLengthValidator(1), MaxLengthValidator(limit_value=16)],
    )
    email = models.EmailField(verbose_name="Email Address", unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email} - {self.username}"
