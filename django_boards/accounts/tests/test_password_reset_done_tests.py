from django.contrib.auth import views as auth_views
from django.urls import reverse
from django.urls import resolve
from django.test import TestCase

class PasswordResetDoneTests(TestCase):
    def setUp(self):
        url = reverse('password_reset_done')
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_view_function(self):
        view = resolve('/password-reset/done/')
        self.assertEqual(view.func.view_class, auth_views.PasswordResetDoneView)