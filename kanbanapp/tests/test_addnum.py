from django.test import TestCase

def addnum(x,y):
    return x+y

class MyTests(TestCase):

    def test_add_numbers(self):

        self.assertEqual(addnum(3, 8), 11)

