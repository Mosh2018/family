from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

CREATE_USER_URL = reverse('user:create')
TOKEN_URL = reverse('user:token')

payload = {
    'email': 'mohamid@gamial.com',
    'username': 'Mohamid',
    'password': '1234pass'
}


def create_user(**param):
    return get_user_model().objects.create_user(**param)


class AbstractTest(TestCase):

    def setUp(self):
        self.client = APIClient()
