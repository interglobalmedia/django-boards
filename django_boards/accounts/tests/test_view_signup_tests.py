from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse

from ..forms import SignUpForm
from ..views import signup

import bs4
import soupsieve as sv


class SignUpTests(TestCase):
    def setUp(self):
        url = reverse("signup")
        self.response = self.client.get(url)

    def test_signup_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        view = resolve("/signup/")
        self.assertEqual(view.func, signup)

    def test_csrf(self):
        self.assertContains(self.response, "csrfmiddlewaretoken")

    def test_contains_form(self):
        form = self.response.context.get("form")
        self.assertIsInstance(form, SignUpForm)

    def test_form_inputs(self):
        """
        The view must contain five inputs: csrf, username, email, password1, password2
        """
        self.assertContains(self.response, "<input", 7)

        # added to the bottom of the (refactored) test_form_inputs test:
        self.response = self.client.get(reverse("signup"))
        text = """
        <form method="post" novalidate="" class="signup-form">
            <input type="hidden" name="csrfmiddlewaretoken" value="5bzfyc9iidGoyInd3IYNlTrBGVLNVo09hNqsSjydsbrvupjtRELqgD8siJf94pup">

            <div class="form-group">
                <label for="id_username">Username:</label>
                <input type="text" name="username" maxlength="150" autofocus="" class="form-control " required="" aria-describedby="id_username_helptext" id="id_username" data-np-intersection-state="visible">
                
                <small class="form-text text-muted">
                    Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
                </small>
            </div>

            <div class="form-group">
                <label for="id_email">Email:</label>
                <input type="email" name="email" maxlength="254" class="form-control " required="" id="id_email" data-np-intersection-state="visible">
            </div>

            <div class="form-group">
                <label for="id_password1">Password:</label>
                <input type="password" name="password1" autocomplete="new-password" class="form-control " aria-describedby="id_password1_helptext" id="id_password1" data-np-intersection-state="visible">
                
                
                <small class="form-text text-muted">
                    <ul><li>Your password can’t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can’t be a commonly used password.</li><li>Your password can’t be entirely numeric.</li></ul>
                </small>
                
            </div>

            <div class="form-group">
                <label for="id_password2">Password confirmation:</label>
                <input type="password" name="password2" autocomplete="new-password" class="form-control " aria-describedby="id_password2_helptext" id="id_password2" data-np-intersection-state="visible">
                
                
                <small class="form-text text-muted">
                    Enter the same password as before, for verification.
                </small>
                
            </div>

            <div class="form-group">
                <label>Password-based authentication:</label>
                <div id="id_usable_password" class="form-control "><div>
                <label for="id_usable_password_0"><input type="radio" name="usable_password" value="true" class="form-control " id="id_usable_password_0" checked="">
            Enabled</label>

            </div>
            <div>
                <label for="id_usable_password_1"><input type="radio" name="usable_password" value="false" class="form-control " id="id_usable_password_1">
            Disabled</label>

            </div>
            <div>
                <small class="form-text text-muted">
                    Whether the user will be able to authenticate using a password or not. If disabled, they may still be able to authenticate using other backends, such as Single Sign-On or LDAP.
                </small>
            </div>

            <button type="submit" class="btn btn-primary btn-block">Create an account</button>
        </form>
        """
        soup = bs4.BeautifulSoup(text, "html5lib")
        sv.select(
                "form:is(.signup-form)",
                soup,
        )
        print(
            sv.select(
                "form:is(.signup-form)",
                soup,
            )
        )
        for tag in soup.find_all('input'):
            print(tag)


class SuccessfulSignUpTests(TestCase):
    def setUp(self):
        url = reverse("signup")
        data = {
            "username": "john",
            "email": "john@doe.com",
            "password1": "abcdef123456",
            "password2": "abcdef123456",
        }
        self.response = self.client.post(url, data)
        self.index_url = reverse("index")

    def test_redirection(self):
        """
        A valid form submission should redirect the user to the home page
        """
        self.assertRedirects(self.response, self.index_url)

    def test_user_creation(self):
        self.assertTrue(User.objects.exists())

    def test_user_authentication(self):
        """
        Create a new request to an arbitrary page.
        The resulting response should now have an `user` to its context, after a successful sign up.
        """
        response = self.client.get(self.index_url)
        user = response.context.get("user")
        self.assertTrue(user.is_authenticated)


class InvalidSignUpTests(TestCase):
    def setUp(self):
        url = reverse("signup")
        self.response = self.client.post(url, {})  # submit an empty dictionary

    def test_signup_status_code(self):
        """
        An invalid form submission should return to the same page
        """
        self.assertEqual(self.response.status_code, 200)

    def test_form_errors(self):
        form = self.response.context.get("form")
        self.assertTrue(form.errors)

    def test_dont_create_user(self):
        self.assertFalse(User.objects.exists())
