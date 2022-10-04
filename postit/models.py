from django.db import models

# Create your models here.

# this model/class is for the id/content whn users will post


class Postit(models.Model):
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
