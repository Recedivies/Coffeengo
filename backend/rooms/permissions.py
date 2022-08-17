from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.views import APIView

from rooms.models import Room

PROTECTED_METHODS = ["PUT", "PATCH", "DELETE"]
ALLOWED_METHODS = ["GET", "HEAD", "OPTIONS", "POST"]


class IsHostOrListCreateOnly(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: APIView, obj: Room) -> bool:
        if request.method in PROTECTED_METHODS:
            if obj.host and obj.host == request.user:
                return True
        elif request.method in ALLOWED_METHODS:
            return True
        return False
