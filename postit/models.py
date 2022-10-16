import random
from django.conf import settings
from django.db import models

# Create your models here.

User = settings.AUTH_USER_MODEL


class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey("Postit", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
# this model/class is for the id/content whn users will post


class Postit(models.Model):
    # Map to SQL Data
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # I want to delete everything from a user if user is deleted
    likes = models.ManyToManyField(
                                    User,
                                    related_name='post_user',
                                    blank=True,
                                    through=PostLike
                                    )
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    @property
    def is_share(self):
        return self.parent != None

