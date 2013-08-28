"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

"""

from django.test import TestCase, Client
from game.models import Drawing, Caption

class WebTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_has_canvas(self):
        res = self.client.get('/')
        self.assertIn('canvas', res.content)


class ModelTest(TestCase):
	def setUp(self):
		self.drawing = Drawing()
		self.caption = Caption(previous=self.drawing)
		self.drawing.previous = self.caption

	def test_previous_drawing(self):
		self.assertEquals(self.drawing.previous, self.caption)

	def test_previous_caption(self):
		self.assertEquals(self.caption.previous, self.drawing)