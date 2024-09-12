from django.urls import reverse
from django.test import TestCase
from django.urls import resolve
from .views import index, board_topics, new_topic
from .models import Board

# Create your tests here.

class IndexTests(TestCase):

  def setUp(self):
    self.board = Board.objects.create(name='Python', description='Everything related to Python')
    url = reverse('index')
    self.response = self.client.get(url)

  def test_index_view_status_code(self):
    self.assertEqual(self.response.status_code, 200)

  def test_index_url_resolves_index_view(self):
    view = resolve('/')
    self.assertEqual(view.func, index)

  def test_index_view_contains_link_to_topics_page(self):
    board_topics_url = reverse('board_topics', kwargs={'id': self.board.id})
    self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))

  def test_board_topics_view_contains_link_back_to_index_page(self):
    board_topics_url = reverse('board_topics', kwargs={'id': 1})
    response = self.client.get(board_topics_url)
    index_page_url = reverse('index')
    self.assertContains(response, 'href="{0}"'.format(index_page_url))

class BoardTopicsTests(TestCase):

  def setUp(self):
    Board.objects.create(name='Python', description='Everything related to Python')

  def test_board_topics_view_success_status_code(self):
    url = reverse('board_topics', kwargs={'id': 1})
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_board_topics_view_not_found_status_code(self):
    url = reverse('board_topics', kwargs={'id': 99})
    response = self.client.get(url)
    self.assertEqual(response.status_code, 404)

  def test_board_topics_url_resolves_board_topics_view(self):
    view = resolve('/boards/1/')
    self.assertEqual(view.func, board_topics)

class NewTopicTests(TestCase):

  def setUp(self):
    Board.objects.create(name='Python', description='Everything related to Python')

  def test_new_topic_view_success_status_code(self):
    url = reverse('new_topic', kwargs={'id': 1})
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_new_topic_view_not_found_status_code(self):
    url = reverse('new_topic', kwargs={'id': 99})
    response = self.client.get(url)
    self.assertEqual(response.status_code, 404)

  def test_new_topic_url_resolves_new_topic_view(self):
    view = resolve('/boards/1/new/')
    self.assertEqual(view.func, new_topic)

  def test_new_topic_view_contains_link_back_to_board_topics_view(self):
    new_topic_url = reverse('new_topic', kwargs={'id': 1})
    board_topics_url = reverse('board_topics', kwargs={'id': 1})
    response = self.client.get(new_topic_url)
    self.assertContains(response, 'href="{0}'.format(board_topics_url))

