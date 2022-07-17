from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token


def get_and_authenticate_user(username, password):
    user = authenticate(username=username, password=password)
    if user is None:
        raise serializers.ValidationError(
            "Invalid username/password. Please try again!"
        )
    return user


def create_user_account(username, email, password1, **extra_fields):
    user = get_user_model().objects.create_user(
        username=username, email=email, password=password1, **extra_fields
    )
    return user


def destroy_token(token):
    Token.objects.filter(key=token).delete()
