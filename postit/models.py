import random
from django.conf import settings
from django.db import models

# Create your models here.

User = settings.AUTH_USER_MODEL

# this model/class is for the id/content whn users will post


class Postit(models.Model):
    # Map to SQL Data
    user = models.ForeignKey(User, on_delete=models.CASCADE) # I want to delete everything from a user if user is deleted
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 200)
        }
