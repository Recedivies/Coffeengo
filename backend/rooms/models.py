from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

User = get_user_model()


class Room(models.Model):
    class Status(models.TextChoices):
        WAITING = "WAITING"
        STARTING = "STARTING"
        IN_PROGRESS = "IN_PROGRESS"
        FINISHED = "FINISHED"

    name = models.CharField("Room Name", max_length=16, unique=True)

    password = models.CharField("Password", max_length=20, null=True, blank=True)

    slots = models.PositiveIntegerField(
        "Slots", default=1, validators=[MinValueValidator(1), MaxValueValidator(10)]
    )

    status = models.CharField(
        "Status Room", max_length=15, choices=Status.choices, default=Status.WAITING
    )

    created_at = models.DateTimeField("Date Room created", auto_now_add=True)

    updated_at = models.DateTimeField("Date Room updated", auto_now=True)

    host = models.ForeignKey(
        to=User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="rooms",
        related_query_name="rooms",
    )

    users = models.ManyToManyField(
        to=User,
        through="UserInRoom",
        related_name="usersInRoom",
        related_query_name="usersInRoom",
    )

    class Meta:
        """Meta definition for Room."""

        verbose_name = "Room"
        verbose_name_plural = "Rooms"

    def __str__(self) -> str:
        """Unicode representation of Room."""
        return f"{self.name} - {self.users.all().count()}/{self.slots} - {self.status.lower()}"


class UserInRoom(models.Model):
    """ManyToMany Through Rooms and Users."""

    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)
    joined_at = models.DateTimeField("Date time joined", auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for UserInRoom."""

        verbose_name = "User in Room"
        verbose_name_plural = "Users in Room"

    def __str__(self) -> str:
        return f"{self.user.username} - {self.room.name}"
