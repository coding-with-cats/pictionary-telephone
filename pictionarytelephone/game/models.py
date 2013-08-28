import base64

from django.db import models

class Drawing(models.Model):

    _image = models.TextField(
            db_column='image',
            blank=True)

    @property
    def image(self):
        return base64.decodestring(self._image)

    @image.setter
    def image(self, image):
        self._image = base64.encodestring(image)

    previous = models.ForeignKey("Caption")

class Caption(models.Model):
	previous = models.ForeignKey("Drawing")
	content = models.CharField(max_length='500')
    