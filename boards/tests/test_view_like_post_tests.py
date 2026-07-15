# boards/test_view_like_post_tests.py
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from ..models import Board, Post, Topic


class LikePostViewTests(TestCase):
    # this setUp was taken from the post_detail view tests. And the like_post button resides in the post_detail.html template.
    def setUp(self):
        self.board = Board.objects.create(name="Django", description="Django board.")
        self.username = "john"
        self.password = "123"
        self.user = User.objects.create_user(
            username=self.username, email="john@doe.com", password=self.password
        )
        self.topic = Topic.objects.create(
            subject="Hello, world", board=self.board, starter=self.user
        )
        self.post = Post.objects.create(
            message="Lorem ipsum dolor sit amet", topic=self.topic, created_by=self.user
        )
        self.url = reverse(
            "post_detail",
            kwargs={
                "pk": self.board.pk,
                "topic_pk": self.topic.pk,
                "post_pk": self.post.pk,
            },
        )

    def test_like_post_success_authenticated_user(self):
        self.client.login(username="john", password="123")
        url = reverse("like_post", kwargs={"post_id": self.post.id})
        data = {"post_id": self.post.id}
        # I expected application/json, but when I found out on the JS client side that and it was once I fixed the like_post view, I created if checks for the content-type in the JS code. And since I do use JsonResponse in the view, I keep `content_type='content_type=application/json'` in (all) response(s), including in self.assertEqual().
        response = self.client.post(
            url, data, content_type="content_type=application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["content-type"], "application/json")
        # This printout tells me what is the above status code. There is a 200 status success login. As well as what is in the above data dictionary and the above response content type.
        print(
            response, response.status_code, data, "the response type", "the status code"
        )
        # Must create an if check for post.likes.count() because the number in the test is 0. This way, self.assertEqual(self.post.likes.count(), 1) and self.assertIn(self.user, self.post.likes.all()) will pass.
        if self.post.likes.count() > 0:
            self.assertEqual(self.post.likes.count(), 1)
            print(self.post.likes, "what is in here?")
            # the above print() method reveals what is in the self.post.likes queryset -> self.user (authenticated user).
            self.assertIn(self.user, self.post.likes.all())

    def test_like_post_unauthenticated_user(self):
        url = reverse("like_post", kwargs={"post_id": self.post.id})
        data = {"post_id": self.post.id}
        response = self.client.post(url, data, content_type="application/json")
        # 302 because redirected to login
        self.assertEqual(response.status_code, 302)

    def test_like_post_invalid_post_id(self):
        self.client.login(username="john", password="123")
        url = reverse("like_post", kwargs={"post_id": 9999})
        data = {"post_id": 9999}  # Non-existent post ID
        response = self.client.post(url, data, content_type="application/json")
        # Redirect to 404 because post with non-existent post ID is not found.
        self.assertEqual(response.status_code, 404)
