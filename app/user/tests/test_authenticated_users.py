from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from app.user.tests.abstarct_test import create_user, payload, ME_URL


class PrivateUserApiTests(TestCase):
    """Test api requests that required authentication"""

    def setUp(self):
        self.user = create_user(**payload)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_retrieve_profile_success(self):
        """Test retrieving profile for logged in used"""
        response = self.client.get(ME_URL)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'username': payload['username'],
            'email': payload['email'],
        })

    def test_post_not_allowed(self):
        """Test that POST not allowed on the me url"""

        response = self.client.post(ME_URL, {})
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_user_profile(self):
        """Test updating user profile for authenticated user"""
        payload_2 = {
            'username': 'Mohamid',
            'email': 'Moha@gamial.com',
            'password': '6789pass'
        }
        response = self.client.put(ME_URL, payload_2)

        self.user.refresh_from_db()

        self.assertEqual(self.user.username, payload_2['username'])
        self.assertEqual(self.user.email, payload_2['email'])
        self.assertTrue(self.user.check_password(payload_2['password']))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
