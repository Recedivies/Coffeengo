from django.contrib import admin

from rooms.models import Room, UserInRoom


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    """Admin View for Room"""

    model = Room
    list_display = ("id", "name", "password", "slots", "status", "host")
    list_filter = ("status", "slots")
    fieldsets = (
        (
            "Profile",
            {"fields": ("name", "password", "slots", "status", "host")},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("name", "password", "slots", "status", "host", "users"),
            },
        ),
    )


@admin.register(UserInRoom)
class UserInRoomAdmin(admin.ModelAdmin):
    """Admin View for UserInRoom"""

    list_display = ("id", "room", "user", "joined_at", "last_active")
    readonly_fields = (
        "joined_at",
        "last_active",
    )
