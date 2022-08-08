from django.contrib.auth import get_user_model, logout
from django.core.exceptions import ImproperlyConfigured
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from users import serializers
from users.utils import create_user_account, destroy_token, get_and_authenticate_user

User = get_user_model()


class AuthViewSet(viewsets.GenericViewSet):
    """
    POST    api/auth/login             - login user
    POST    api/auth/register          - register user
    POST    api/auth/password/change   - change password user
    GET     api/auth/me                - retrieve user
    """

    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = serializers.EmptySerializer
    serializer_classes = {
        "login": serializers.UserLoginSerializer,
        "register": serializers.UserRegisterSerializer,
        "password_change": serializers.PasswordChangeSerializer,
        "me": serializers.MeSerializer,
    }

    @action(methods=["POST"], detail=False)
    def login(self, request: Request) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_and_authenticate_user(**serializer.validated_data)
        data = serializers.AuthUserSerializer(user).data
        return Response(data=data, status=status.HTTP_201_CREATED)

    @action(methods=["POST"], detail=False)
    def register(self, request: Request) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_user_account(**serializer.validated_data)
        data = serializers.AuthUserSerializer(user).data
        return Response(data=data, status=status.HTTP_201_CREATED)

    @action(
        methods=["POST"], detail=False, permission_classes=[permissions.IsAuthenticated]
    )
    def logout(self, request: Request) -> Response:
        destroy_token(request.auth)
        logout(request)
        data = {"success": "Sucessfully logged out"}
        return Response(data=data, status=status.HTTP_200_OK)

    @action(
        methods=["POST"],
        detail=False,
        permission_classes=[permissions.IsAuthenticated],
        url_path="password/change",
    )
    def password_change(self, request: Request) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data["new_password"])
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(
        methods=["GET"],
        detail=False,
        permission_classes=[permissions.IsAuthenticated],
    )
    def me(self, request: Request) -> Response:
        serializer = self.get_serializer(request.user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def get_serializer_class(self):
        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes should be a dict mapping.")

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]
        return super().get_serializer_class()
