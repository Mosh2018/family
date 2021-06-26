from django.contrib.auth import get_user_model
from rest_framework import status

from app.user.tests.abstarct_test import AbstractTest
from app.user.tests.abstarct_test import payload, create_user
from app.user.tests.abstarct_test import CREATE_USER_URL


class PublicUserApiTests(AbstractTest):
    """Test the users API"""

    def test_create_user_success(self):
        """Test user with valid payload is success"""
        payload2 = {
            'email': 'mohamid2@gamial.com',
            'username': 'Mohamid2',
            'password': '1234pass'
        }

        res = self.client.post(CREATE_USER_URL, payload2)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload2['password']))
        self.assertNotIn('password', res.data)

    def test_user_exists(self):
        """Test creating user that is already exist """
        create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """Test that password must be more than 8 characters"""

        payload['password'] = 'pwd'
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

        user_exist = get_user_model().objects.filter(
            username=payload['username']
        ).exists()
        self.assertFalse(user_exist)
