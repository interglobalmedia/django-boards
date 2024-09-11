from django.urls import reverse
from django.test import TestCase
from django.urls import resolve
from .views import index, board_topics
from .models import Board

# Create your tests here.

class IndexTests(TestCase):

  def test_index_view_status_code(self):
    url = reverse('index')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_index_url_resolves_index_view(self):
    view = resolve('/')
    self.assertEqual(view.func, index)

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

