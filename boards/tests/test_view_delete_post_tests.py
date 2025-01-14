from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from ..models import Board, Post, Topic
from ..views import PostDeleteView


class PostDeleteViewTestCase(TestCase):
    """
    Base test case to be used in all `PostDeleteView` view tests
    """

    def setUp(self):
        self.board = Board.objects.create(name="Django", description="Django board.")
        self.username = "john"
        self.password = "123"
        user = User.objects.create_user(
            username=self.username, email="john@doe.com", password=self.password
        )
        self.topic = Topic.objects.create(
            subject="Hello, world", board=self.board, starter=user
        )
        self.post = Post.objects.create(
            message="Lorem ipsum dolor sit amet", topic=self.topic, created_by=user
        )
        self.url = reverse(
            "delete_post",
            kwargs={
                "pk": self.board.pk,
                "topic_pk": self.topic.pk,
                "post_pk": self.post.pk,
            },
        )


class LoginRequiredPostDeleteViewTests(PostDeleteViewTestCase):
    def test_redirection(self):
        """
        Test if only logged in users can delete the posts
        """
        login_url = reverse("login")
        response = self.client.get(self.url)
        self.assertRedirects(
            response, "{login_url}?next={url}".format(login_url=login_url, url=self.url)
        )


class UnauthorizedPostDeleteViewTests(PostDeleteViewTestCase):
    def setUp(self):
        """
        Create a new user different from the one who posted
        """
        super().setUp()
        username = "jane"
        password = "321"
        user = User.objects.create_user(
            username=username, email="jane@doe.com", password=password
        )
        self.client.login(username=username, password=password)
        self.response = self.client.get(self.url)

    def test_status_code(self):
        """
        A topic should be deleted only by the owner.
        Unauthorized users should get a 404 response (Page Not Found)
        """
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 404)
