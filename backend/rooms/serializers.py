from rest_framework import serializers

from rooms.models import Room
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class RoomSerializer(serializers.ModelSerializer):
    host = UserSerializer(read_only=True)
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ("id", "name", "password", "slots", "host", "users")


class CreateRoomSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=16, required=True)
    password = serializers.CharField(max_length=20, required=False, allow_blank=True)
    slots = serializers.IntegerField(min_value=1, max_value=10, required=True)
