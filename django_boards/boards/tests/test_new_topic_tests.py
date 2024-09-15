from django.urls import reverse
from django.test import TestCase
from django.urls import resolve
from django.contrib.auth.models import User
from ..views import index, board_topics, new_topic
from ..models import Board, Topic, Post
from ..forms import NewTopicForm

class NewTopicTests(TestCase):

    def setUp(self):
        Board.objects.create(name="Python", description="Everything related to Python")
        User.objects.create_user(username='jane', email='jane@doe.com', password='123')

    def test_csrf(self):
        url = reverse('new_topic', kwargs={'id': 1})
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_new_topic_valid_post_data(self):
        url = reverse('new_topic', kwargs={'id': 1})
        data = {
            'subject': 'Test title',
            'message': 'Lorem ipsum dolor sit amet'
        }
        response = self.client.post(url, data)
        self.assertTrue(Topic.objects.exists())
        self.assertTrue(Post.objects.exists())

    def test_new_topic_invalid_post_data(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('new_topic', kwargs={'id': 1})
        response = self.client.post(url, {})
        self.assertEqual(response.status_code, 200)

    def test_new_topic_invalid_post_data_empty_fields(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('new_topic', kwargs={'id': 1})
        data = {
            'subject': '',
            'message': ''
        }