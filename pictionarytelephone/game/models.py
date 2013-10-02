from django.db import models

class Drawing(models.Model):
    image = models.TextField(blank=True)
    previous = models.ForeignKey("Caption")

class Caption(models.Model):
	previous = models.ForeignKey("Drawing", null=True)
	content = models.CharField(max_length='500')
