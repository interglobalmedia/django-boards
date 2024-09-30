from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Board
from ..views import index

class IndexTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')
        url = reverse('index')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEqual(view.func, index)

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={'id': self.board.id})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))