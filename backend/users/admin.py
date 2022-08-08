from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from users.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    model = User
    list_display = ("id", "username", "email", "is_superuser", "is_staff", "is_active")
    list_filter = ("username", "is_staff", "is_active")
    fieldsets = (
        ("Profile", {"fields": ("username", "email", "password")}),
        ("Permissions", {"fields": ("is_superuser", "is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = ("username",)
    ordering = ("username",)


admin.site.unregister(Group)
