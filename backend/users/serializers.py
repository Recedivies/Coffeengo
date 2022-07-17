from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.models import BaseUserManager
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()


class EmptySerializer(serializers.Serializer):
    pass


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=16, required=True)
    password = serializers.CharField(required=True, write_only=True)


class AuthUserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("token",)

    def get_token(self, obj):
        token = Token.objects.filter(user=obj)
        if token.count() == 0:
            token = Token.objects.create(user=obj)
            return token.key
        new_key = token[0].generate_key()
        token.update(key=new_key)

        return token[0].key


class UserRegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(
        label="Password",
        write_only=True,
        style={
            "input_type": "password",
        },
    )
    password2 = serializers.CharField(
        label="Confirm Password", write_only=True, style={"input_type": "password"}
    )

    class Meta:
        model = User
        fields = ("id", "username", "email", "password1", "password2")
        extra_kwargs = {
            "password2": {"write_only": True},
        }

    def validate(self, attrs):
        if attrs["password1"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        del attrs["password2"]
        return attrs

    def validate_email(self, email):
        user = User.objects.filter(email=email)
        if user:
            raise serializers.ValidationError("Email is already taken")
        return BaseUserManager.normalize_email(email)

    def validate_password1(self, value):
        password_validation.validate_password(value)
        return value


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_current_password(self, value):
        if not self.context["request"].user.check_password(value):
            raise serializers.ValidationError("Current password does not match")
        return value

    def validate_new_password(self, value):
        password_validation.validate_password(value)
        return value


class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")
