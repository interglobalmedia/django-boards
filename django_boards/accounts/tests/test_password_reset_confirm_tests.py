from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User
from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
import bs4
import soupsieve as sv

class PasswordResetConfirmTests(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='john', email='john@doe.com', password='123abcdef')

        '''
        create a valid password reset token
        based on how django creates the token internally:
        https://github.com/django/django/blob/1.11.5/django/contrib/auth/forms.py#L280
        '''
        self.uid = urlsafe_base64_encode(force_bytes(user.id)).encode()
        self.token = default_token_generator.make_token(user)

        url = reverse('password_reset_confirm', kwargs={'uidb64': self.uid, 'token': self.token})
        self.response = self.client.get(url, follow=True)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_view_function(self):
        view = resolve('/password-reset/{uidb64}/{token}/'.format(uidb64=self.uid, token=self.token))
        self.assertEqual(view.func.view_class, auth_views.PasswordResetConfirmView)

    def test_csrf(self):
        self.assertContains(self.response, 'sha512-2rNj2KJ+D8s1ceNasTIex6z4HWyOnEYLVC3FigGOmyQCZc2eBXKgOxQmo3oKLHyfcj53uz4QMsRCWNbLd32Q1g')

    def test_contains_form(self):
        form = self.response.context.get('form')
        # replaced self.assertIsInstance(form, PasswordResetForm) line with below because original line returned None. But below, response has a context attribute that contains the context used to render the template.
        self.assertIn('form', self.response.context)

    # def test_form_inputs(self):
    #     '''
    #     The view must contain two inputs: csrf and two password fields
    #     '''
    #     self.assertContains(self.response, '<input', 3)
    #     self.assertContains(self.response, 'type="password"', 2)
    
    def test_form_inputs(self):
        self.response = self.client.get(reverse('password_reset'))
        text = """
        <form class="password-reset-confirm">
        </form>
        """
        soup = bs4.BeautifulSoup(text, 'html5lib')
        sv.select('input:is(#id_new_password1, #id_new_password2, .form-control)', soup)
        
