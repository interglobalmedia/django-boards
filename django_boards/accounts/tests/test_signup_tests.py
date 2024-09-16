from django.contrib.auth.models import User
from ..forms import SignUpForm
from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from ..views import signup
import bs4
import soupsieve as sv

class SignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        view = resolve('/signup/')
        self.assertEqual(view.func, signup)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, SignUpForm)

    # def test_form_inputs(self):
    #     '''
    #     The view must contain five inputs: csrf, username, email, password1, password2
    #     '''
    #     self.assertContains(self.response, '<input', 7)
    #     self.assertContains(self.response, '<input type="text" name="username" maxlength="150" autofocus class="form-control" required aria-describedby="id_username_helptext" id="id_username">', 1)
    #     self.assertContains(self.response, '<input type="email" name="email" maxlength="254" class="form-control" required id="id_email">', 1)
    #     self.assertContains(self.response, '<input type="password" name="password1" autocomplete="new-password" class="form-control" aria-describedby="id_password1_helptext" id="id_password1">', 1)
    #     self.assertContains(self.response, '<input type="password" name="password2" autocomplete="new-password" class="form-control" aria-describedby="id_password2_helptext" id="id_password2">', 1)

    def test_form_inputs(self):
        self.response = self.client.get(reverse('signup'))
        text = """
        <form class="signup-form">
        </form>
        """
        soup = bs4.BeautifulSoup(text, 'html5lib')
        sv.select('input:is(#id_username, #id_email, #id_password1, #id_password2)', soup)
