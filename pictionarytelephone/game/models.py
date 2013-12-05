from django.db import models

class Drawing(models.Model):
    image = models.TextField(blank=True)
    previous = models.ForeignKey("Caption")
    user = models.ForeignKey("User")

class Caption(models.Model):
    previous = models.ForeignKey("Drawing", null=True)
    content = models.CharField(max_length='500')
    user = models.ForeignKey("User")

class User(models.Model):
    pass
