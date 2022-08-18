import random
import string

from django.contrib.auth import get_user_model
from django.test import SimpleTestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from rooms.models import Room

User = get_user_model()


class ApiUrlsTests(SimpleTestCase):
    def test_get_rooms_url(self):
        url = reverse("rooms-list")
        self.assertEqual(url, "/api/rooms")


class RoomTests(APITestCase):
    room_url = reverse("rooms-list")

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="user",
            email="user@gmail.com",
            password="user3231",
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def name_generator(self):
        return "".join(
            random.choice(string.ascii_uppercase + string.digits) for _ in range(8)
        )

    def create_room(self, room_name=""):
        if room_name:
            Room.objects.create(name=room_name, password="", slots=9)
            return

        name = self.name_generator()
        while Room.objects.filter(name=name).exists():
            name = self.name_generator()
        Room.objects.create(name=name, password="", slots=9)

    def test_create_room(self):
        data = {"name": "room1", "password": "3231", "slots": 5}
        response = self.client.post(self.room_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Room.objects.count(), 1)

    def test_create_room_host_already_hosted_room(self):
        data = {"name": "room1", "password": "3231", "slots": 5}
        self.client.post(self.room_url, data, format="json")
        data["name"] = "room2"
        response = self.client.post(self.room_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_room_empty_name(self):
        data = {"name": "", "password": "3231", "slots": 5}
        response = self.client.post(self.room_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Room.objects.count(), 0)

    def test_list_rooms(self):
        response = self.client.get(self.room_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Room.objects.count(), 0)
        self.create_room()
        self.assertEqual(Room.objects.count(), 1)

    def test_retrieve_room(self):
        self.create_room(room_name="test")
        response = self.client.get(self.room_url + "/test", format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(Room.objects.get(name="test"))

    def test_update_room(self):
        self.create_room(room_name="test")
        data = {"name": "room1", "password": "3231", "slots": 5}
        response = self.client.put(self.room_url + "/test", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(Room.objects.get(name="room1"))
        self.assertFalse(Room.objects.filter(name="test").exists())

    def test_partial_update_room(self):
        self.create_room(room_name="test")
        data = {"name": "new_room"}
        response = self.client.put(self.room_url + "/test", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(Room.objects.get(name="new_room"))
        self.assertFalse(Room.objects.filter(name="test").exists())

    def test_delete_room(self):
        self.create_room(room_name="test")
        response = self.client.delete(self.room_url + "/test", format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Room.objects.filter(name="test").exists())
