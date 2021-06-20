from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating new user with email is success"""
        username = "Mohamid"
        email = 'moha@gmail.com'
        password = 'olen_password'
        user = get_user_model().objects.create_user(
            username=username,
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_username_normalized(self):
        """Test email for new user is normalized"""
        username = "Mohamid"
        email = 'moha@Gmail.com'
        password = 'olen_password'
        user = get_user_model().objects.create_user(username, email, password)

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_username(self):
        """Test creating new user with no raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'moha@gmail.com', '1234test')

    def test_new_user_invalid_email(self):
        """Test creating new user with no raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('Mohamid', None, '1234test')

    def test_new_superuser_successful(self):
        """Test create superuser is success"""
        username = "Mohamid"
        email = 'moha@gmail.com'
        password = 'olen_password'
        user = get_user_model().objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)