from django.urls import reverse
from django.test import TestCase
from django.urls import resolve
from django.contrib.auth.models import User
from ..views import index, board_topics, new_topic
from ..models import Board, Topic, Post
from ..forms import NewTopicForm

# Create your tests here.

class IndexTests(TestCase):

    def setUp(self):
        self.board = Board.objects.create(
            name="Python", description="Everything related to Python"
        )
        url = reverse("index")
        self.response = self.client.get(url)

    def test_index_view_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_url_resolves_index_view(self):
        view = resolve("/")
        self.assertEqual(view.func, index)

    def test_index_view_contains_link_to_topics_page(self):
        board_topics_url = reverse("board_topics", kwargs={"id": self.board.id})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))

    def test_board_topics_view_contains_link_back_to_index_page(self):
        board_topics_url = reverse("board_topics", kwargs={"id": 1})
        response = self.client.get(board_topics_url)
        index_page_url = reverse("index")
        self.assertContains(response, 'href="{0}"'.format(index_page_url))