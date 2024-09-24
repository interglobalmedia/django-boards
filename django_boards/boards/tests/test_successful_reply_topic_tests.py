from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from ..models import Board, Post, Topic
from ..views import reply_topic
from .test_reply_topic_test_case import ReplyTopicTestCase

class SuccessfulReplyTopicTests(ReplyTopicTestCase):
    def setUp(self):
        super().setUp()
        self.client.login(username=self.username, password=self.password)
        self.response = self.client.post(self.url, {'message': 'hello, world!'})

    def test_redirection(self):
        '''
        A valid form submission should redirect the user
        '''
        topic_posts_url = reverse('topic_posts', kwargs={'id': self.board.id, 'topic_id': self.topic.id})
        self.assertRedirects(self.response, topic_posts_url)

    def test_reply_created(self):
        '''
        The total post count should be 2
        The one created in the `ReplyTopicTestCase` setUp
        and another created by the post data in this class
        '''
        self.assertEqual(Post.objects.count(), 2)