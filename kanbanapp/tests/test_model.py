from django.test import TestCase
from ..models import User

class ModelTests(TestCase):

    def test_create_user(self):
        username = 'testuserharsh'
        password = 'test@123'
        user = User.objects.create_user(username=username, password=password)
        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))

