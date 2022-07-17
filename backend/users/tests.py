from django.contrib.auth import get_user_model
from django.test import SimpleTestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

User = get_user_model()


class ApiUrlsTests(SimpleTestCase):
    def test_get_register_url(self):
        url = reverse("auth-register")
        self.assertEqual(url, "/api/auth/register")

    def test_get_login_url(self):
        url = reverse("auth-login")
        self.assertEqual(url, "/api/auth/login")

    def test_get_logout_url(self):
        url = reverse("auth-logout")
        self.assertEqual(url, "/api/auth/logout")

    def test_get_password_change_url(self):
        url = reverse("auth-password-change")
        self.assertEqual(url, "/api/auth/password_change")

    def test_get_user_url(self):
        url = reverse("auth-me")
        self.assertEqual(url, "/api/auth/me")


class AccountTests(APITestCase):
    register_url = reverse("auth-register")
    login_url = reverse("auth-login")
    logout_url = reverse("auth-logout")
    password_change_url = reverse("auth-password-change")
    me_url = reverse("auth-me")

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="user",
            email="user@gmail.com",
            password="user3231",
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_register(self):
        data = {
            "username": "Recedivies",
            "email": "re@gmail.com",
            "password1": "rece3231",
            "password2": "rece3231",
        }
        response = self.client.post(self.register_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def test_register_password_not_match(self):
        data = {
            "username": "Recedivies",
            "email": "re@gmail.com",
            "password1": "rece3231",
            "password2": "not_match",
        }
        response = self.client.post(self.register_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)

    def test_register_email_already_taken(self):
        data = {
            "username": "Recedivies",
            "email": "user@gmail.com",
            "password1": "rece3231",
            "password2": "rece3231",
        }
        response = self.client.post(self.register_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)

    def test_login(self):
        data = {"username": "user", "password": "user3231"}
        response = self.client.post(self.login_url, data, format="json")
        token = Token.objects.get(user=self.user)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["token"], token.key)

    def test_logout(self):
        response = self.client.post(self.logout_url)
        token = Token.objects.filter(user=self.user)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(token.count(), 0)

    def test_password_change(self):
        data = {"current_password": "user3231", "new_password": "newuser3231"}
        response = self.client.post(self.password_change_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        data_login = {"username": "user", "password": "user3231"}
        response_login = self.client.post(self.login_url, data_login, format="json")

        self.assertEqual(response_login.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_change_password_not_match(self):
        data = {
            "current_password": "not_match_password_user3231",
            "new_password": "newuser3231",
        }
        response = self.client.post(self.password_change_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        data_login = {"username": "user", "password": "user3231"}
        response_login = self.client.post(self.login_url, data_login, format="json")

        self.assertEqual(response_login.status_code, status.HTTP_201_CREATED)

    def test_detail_user(self):
        response = self.client.get(self.me_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "user")
