from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from ..models import Board, Post, Topic


class BoardModelsTests(TestCase):
    # this setUp was taken from the post_detail view tests. And the like_post button resides in the post_detail.html template.
    def setUp(self):
        self.board = Board.objects.create(name="Django", description="Django board.")

    def test_get_posts_count(self):
        board_count = self.board.get_posts_count()
        self.assertEqual(board_count, 0)
