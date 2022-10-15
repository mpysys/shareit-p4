from django.test import TestCase

# Create your tests here.

from Postit.models import Postit, PostLike
Postit.objects.all()
obj = Postit.objects.first()
obj.likes.all()


from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.all()
me = User.objects.first()
obj.likes.add(me)
obj.likes.all()

query_set = USer.objects.all()
obj.likes.set(query_set)
obj.likes.all()