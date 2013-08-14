"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

"""

from django.test import TestCase, Client


class SimpleTest(TestCase):
    def setUp(self):
        self.client = Client()


    def test_has_canvas(self):
        res = self.client.get('/')
        self.assertIn('canvas', res.content)

