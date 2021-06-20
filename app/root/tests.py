from django.test import TestCase


class SimpleTest(TestCase):

    def test_adding_numbers(self):
        """Simple tests"""
        self.assertEqual(1+1, 2)
