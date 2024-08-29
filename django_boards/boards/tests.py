from django.urls import reverse
from django.test import TestCase
from django.urls import resolve
from .views import index

# Create your tests here.

class IndexTests(TestCase):

  def test_index_view_status_code(self):
    url = reverse('index')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

  def test_index_url_resolves_index_view(self):
    view = resolve('/')
    self.assertEqual(view.func, index)
