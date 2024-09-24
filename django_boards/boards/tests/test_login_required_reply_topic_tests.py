from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from ..models import Board, Post, Topic
from ..views import reply_topic
from .test_reply_topic_test_case import ReplyTopicTestCase


class LoginRequiredReplyTopicTests(ReplyTopicTestCase):
    def test_redirection(self):
        login_url = reverse("login")
        response = self.client.get(self.url)
        self.assertRedirects(
            response, "{login_url}?next={url}".format(login_url=login_url, url=self.url)
        )
