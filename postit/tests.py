from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIClient

from .models import Postit
# Create your tests here.
User = get_user_model()

class PostTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='abc', password='somepassword')
        self.userb = User.objects.create_user(username='efg', password='somepassword2')
        Postit.objects.create(content="my initial post", user=self.user)
        Postit.objects.create(content="my other post", user=self.user)
        Postit.objects.create(content="my other (again) post", user=self.userb)
        Postit.objects.create(content="my other (and again) post", user=self.user)
        self.currentCount = Postit.objects.all().count()

    def test_user_create(self):
        self.assertEqual(self.user.username, 'abc')

    def test_post_created(self):
        post_obj = Postit.objects.create(content="my second post", user=self.user)
        self.assertEqual(post_obj.id, 5)
        self.assertEqual(post_obj.user, self.user)

    def get_client(self):
        client = APIClient()
        client.login(username=self.user.username, password='somepassword')
        return client

    def test_post_list(self):
        client = self.get_client()
        response = client.get("/api/postit/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_post_list(self):
        client = self.get_client()
        response = client.get("/api/postit/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 4)

    def test_action_like(self):
        client = self.get_client()
        response = client.post("/api/postit/action/", {"id": 1, "action": "like"})
        self.assertEqual(response.status_code, 200)
        like_count = response.json().get("likes")
        self.assertEqual(like_count, 1)

    def test_action_unlike(self):
        client = self.get_client()
        response = client.post("/api/postit/action/", {"id": 2, "action": "like"})
        response = client.post("/api/postit/action/", {"id": 2, "action": "unlike"})
        self.assertEqual(response.status_code, 200)
        like_count = response.json().get("likes")
        self.assertEqual(like_count, 0)

    def test_action_share(self):
        client = self.get_client()
        response = client.post("/api/postit/action/", {"id": 2, "action": "share"})
        self.assertEqual(response.status_code, 201)
        data = response.json()
        new_post_id = data.get("id")
        self.assertNotEqual(2, new_post_id)
        self.assertEqual(self.currentCount + 1, new_post_id)

    def test_post_create_api_view(self):
        request_data = {"content": "This is a post used for testing"}
        client = self.get_client()
        response = client.post("/api/postit/create/", request_data)
        self.assertEqual(response.status_code, 201)
        response_data = response.json()
        new_post_id = response_data.get("id")
        self.assertEqual(self.currentCount + 1, new_post_id)

    def test_post_detail_api_view(self):
        client = self.get_client()
        response = client.get("/api/postit/1/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        _id = data.get("id")
        self.assertEqual(_id, 1)

    def test_post_delete_api_view(self):
        client = self.get_client()
        response = client.delete("/api/postit/1/delete/")
        self.assertEqual(response.status_code, 200)
        client = self.get_client()
        response = client.delete("/api/postit/1/delete/")
        self.assertEqual(response.status_code, 404)
        response_incorrect_owner = client.delete("/api/postit/3/delete/")
        self.assertEqual(response_incorrect_owner.status_code, 401)
    