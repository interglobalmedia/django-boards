from django.contrib.auth.models import User
from ..forms import SignUpForm
from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from ..views import signup

class SuccessfulSignUpTests(TestCase):

    def setUp(self):
        url = reverse('signup')
        data = {
            'username': 'john',
            'email': 'john@doe.com',
            'password1': 'abcdef123456',
            'password2': 'abcdef123456'
        }
        self.response = self.client.post(url, data)
        self.index_url = reverse('index')

    def test_redirection(self):
        '''
        A valid form submission should redirect the user to the home page
        '''
        self.assertRedirects(self.response, self.index_url)

    def test_user_creation(self):
        self.assertTrue(User.objects.exists())

    def test_user_authentication(self):
        '''
        Create a new request to an arbitrary page.
        The resulting response should now have a `user` to its context,
        after a successful sign up.
        '''
        response = self.client.get(self.index_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)


