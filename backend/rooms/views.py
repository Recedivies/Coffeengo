from typing import Any

from django.contrib.auth import get_user_model
from django.core.exceptions import ImproperlyConfigured
from django.db.models import QuerySet
from rest_framework import permissions, status, viewsets

# from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from rooms import serializers
from rooms.models import Room
from rooms.utils import create_room
from utils.response import response_message

User = get_user_model()


class RoomViewSet(viewsets.ModelViewSet):
    """
    GET     api/rooms                   - list all rooms
    POST    api/rooms                   - create room
    GET     api/rooms/<str:name>/       - retrieve room
    PUT     api/rooms/<str:name>/       - update room attr
    PATCH   api/rooms/<str:name>/       - partially update room
    DELETE  api/rooms/<str:name>/       - delete room

    GET     api/rooms/<str:name>/user   - check if current user in this room
    POST    api/rooms/<str:name>/join   - current user join room
    DELETE  api/rooms/<str:name>/leave  - current user leave room
    """

    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = serializers.RoomSerializer
    serializer_classes = {
        "create": serializers.RoomSerializer,
    }
    lookup_field = "name"

    def get_queryset(self) -> QuerySet[Room]:
        return Room.objects.all().prefetch_related("users")

    def get_serializer_class(self):
        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes should be a dict mapping.")
        # if hasattr(self, "action") and self.action in ["list", "retrieve"]:
        #     return DetailedRoomSerializer
        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action == "create":
            return [permissions.IsAuthenticated()]
        return super(RoomViewSet, self).get_permissions()

    def list(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(
            response_message(message="", content=serializer.data, success=True),
            status=status.HTTP_200_OK,
        )

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        user = request.user
        is_already_hosted = Room.objects.filter(status="WAITING", host=user)
        if is_already_hosted.exists():
            return Response(
                response_message(
                    message="Host already hosted in another room",
                    content=None,
                    success=False,
                ),
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_room(**serializer.validated_data, host=user)
        return Response(
            response_message(message="", content=None, success=True),
            status=status.HTTP_201_CREATED,
        )

    def retrieve(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer = self.get_serializer(self.get_object(), many=False)
        return Response(
            response_message(message="", content=serializer.data, success=True),
            status=status.HTTP_200_OK,
        )

    def update(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        partial = kwargs.pop("partial", False)
        room = self.get_object()
        serializer = self.get_serializer(
            instance=room, data=request.data, partial=partial
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(
            response_message(
                message="resource updated successfully",
                content="",
                success=True,
            ),
            status=status.HTTP_200_OK,
        )

    def partial_update(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        kwargs["partial"] = True
        return self.update(request, *args, **kwargs)

    def destroy(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        room = self.get_object()
        self.perform_destroy(instance=room)
        return Response(
            response_message(
                message="resource deleted successfully",
                content="",
                success=True,
            ),
            status=status.HTTP_204_NO_CONTENT,
        )
