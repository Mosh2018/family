from rest_framework import status

from app.user.tests.abstarct_test import AbstractTest
from app.user.tests.abstarct_test import payload, create_user
from app.user.tests.abstarct_test import TOKEN_URL


class AuthTokenTest(AbstractTest):
    """Test Auth Token for user"""

    def test_create_auth_token(self):
        create_user(**payload)
        response = self.client.post(TOKEN_URL, payload)

        self.assertIn('token', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_token_invalid_credentials(self):
        """Test that token is not created if invalid credential are given """
        create_user(**payload)
        payload['password'] = 'WrongPassword'
        response = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_no_user(self):
        """Test token not created if user not exist"""
        response = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_missing_field(self):
        """Test that username and password are required"""
        payload['password'] = ''
        response = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
