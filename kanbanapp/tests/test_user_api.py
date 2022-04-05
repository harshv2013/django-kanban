from django.test import TestCase
from ..models import User
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = 'http://127.0.0.1:8000/user/register/'
LOGIN_USER_URL = 'http://127.0.0.1:8000/user/login/'
# CREATE_USER_URL = reverse('user:create')

def create_user(**params):
    return User.objects.create_user(**params)

class PublicUserApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        payload = {
            "username": "Harsh3",
            "password": "test@123",
            "password2": "test@123",
            "email": "harsh32013@mail.com"
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(**res.data)
        print('user =====',user)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password',res.data)
        self.assertEqual(res.data['username'], 'Harsh3')
        print('res data=======', res.data)

    def test_user_login(self):
        payload = {
            "username": "Harsh3",
            "password": "test@123",
            "password2": "test@123",
            "email": "harsh32013@mail.com"
        }
        res = self.client.post(CREATE_USER_URL, payload)
        payload = {
            "username":"Harsh3",
            "password": "test@123"
        }

        res = self.client.post(LOGIN_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        print('res data======',res.data)

    def test_user_exists(self):
        payload = {
            "username": "Harsh3",
            "password": "test@123",
            "email": "harsh32013@mail.com"
        }
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        payload = {
            "username": "Harsh3",
            "password": "pw",
            "password2": "pw",
            "email": "harsh32013@mail.com"
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = User.objects.filter(
            username=payload['username']
        ).exists()
        self.assertFalse(user_exists)

    def test_create_token_for_user(self):
        payload = {
            "username": "Harsh3",
            "password": "test@123",
            "password2": "test@123",
            "email": "harsh32013@mail.com"
        }
        payload_login = {
            "username": "Harsh3",
            "password": "test@123",
        }

        self.client.post(CREATE_USER_URL, payload)
        res = self.client.post(LOGIN_USER_URL, payload_login)
        print('res *******========',res.data)
        self.assertIn('access', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)







