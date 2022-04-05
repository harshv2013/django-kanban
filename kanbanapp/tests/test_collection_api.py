from django.test import TestCase
from ..models import User
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status
import time

CREATE_USER_URL = 'http://127.0.0.1:8000/user/register/'
LOGIN_USER_URL = 'http://127.0.0.1:8000/user/login/'
COLLECTION_URL = 'http://127.0.0.1:8000/collections/'
BOARD_URL = 'http://127.0.0.1:8000/boards/'
# CREATE_USER_URL = reverse('user:create')

def create_user(**params):
    return User.objects.create_user(**params)

class MyUserApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()

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

    def test_retrive_collection_unauthorized(self):
        res = self.client.get(COLLECTION_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class CollectionAPITests(TestCase):

    def setUp(self):
        payload = {
            "username":"Harsh3",
            "password": "test@123"
        }
        self.user = create_user(**payload)
        self.client = APIClient()
        res = self.client.post(LOGIN_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        print('res data %%%%%%%%%%%%%%%%%%%%%%%%======',res.data)
        # self.client.force_authenticate(user=self.user)
        self.access_token = res.data.get('access')
        print('access-token ========',self.access_token)
        self.headers = {
            'Authorization': f"Bearer {self.access_token}"
            # 'Content-Type': 'application/json'
        }
        self.client.credentials(HTTP_AUTHORIZATION = f"Bearer {self.access_token}")
        payload = {
            "title": "Title of board for unit case.",
            "description": "Description of Board"
        }
        self.res_board = self.client.post(BOARD_URL, payload)

    # def test_retrive_collection(self):
    #     # payload = ''
    #     res = self.client.get(COLLECTION_URL, self.headers)
    #     print('headers=======',self.headers)
    #     print('res at 70====&&&&&&&---&&&&&&=======',res.data)
    #     # self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_board_collection_create_success(self):
        # payload = ''
        self.client.credentials(HTTP_AUTHORIZATION = f"Bearer {self.access_token}")
        payload = {
            "title": "Title of board for unit case.",
            "description": "Description of Board"
        }
        res_board = self.client.post(BOARD_URL, payload)
        print('board create response========', res_board.data)
        self.assertEqual(res_board.status_code, status.HTTP_201_CREATED)
        # time.sleep(2)
        self.assertEqual(res_board.data['owner'], 'Harsh3')
        board_id = res_board.data['id']
        self.assertEqual(board_id, 2)
        # res = self.client.get(BOARD_URL, data={'format': 'json'} )
        res = self.client.get(COLLECTION_URL, {"board_id": board_id})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        # res = self.client.get(COLLECTION_URL)
        print('headers=======',self.headers)
        print('res at 80====&&&&&&&---&&&&&&=======',res.data)

    def test_collection_in_invalid_user(self):
        access_token = ''
        self.client.credentials(HTTP_AUTHORIZATION = f"Bearer {access_token}")
        """ When user (wrong access token) is not valid & board_id is valid."""
        """Error 401"""
        print('board id at line - 103==================',self.res_board.data)
        board_id = self.res_board.data['id']
        res = self.client.get(COLLECTION_URL, {"board_id": board_id})
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_collection_on_wrong_board_id(self):
        """pass wrong board_id for collection api """
        """Error 400"""
        self.client.credentials(HTTP_AUTHORIZATION = f"Bearer {self.access_token}")
        print('board id at line - 103==================',self.res_board.data)
        # board_id = self.res_board.data['id']
        board_id = 900
        res = self.client.get(COLLECTION_URL, {"board_id": board_id})
        print(res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)


    def test_collection(self):
        """When board id user both are valid"""
        """Positive test case status 200"""
        self.client.credentials(HTTP_AUTHORIZATION = f"Bearer {self.access_token}")
        board_id = self.res_board.data['id']
        res = self.client.get(COLLECTION_URL, {"board_id": board_id})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        # print(res.data[0])
        self.assertIn('name', res.data[0])










