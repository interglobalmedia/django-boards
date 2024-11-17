from django.urls import path
from .views import profile, profile_detail, ProfileListView, UserUpdateView
from django.contrib.auth import views

urlpatterns = [
    path('account/', UserUpdateView.as_view(), name='my_account'),
    path("profile/", profile, name="users-profile"),
    path('profile-detail/<int:pk>/', profile_detail, name='profile'),
    path("profiles/", ProfileListView.as_view(), name="users-profile-list"),
    path(
        "login/", views.LoginView.as_view(template_name="login.html"), name="login"
    ),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path(
        "password_reset/",
        views.PasswordResetView.as_view(
            template_name="password_reset.html",
            email_template_name="password_reset_email.html",
            subject_template_name="password_reset_subject.txt",
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        views.PasswordResetDoneView.as_view(
            template_name="password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        views.PasswordResetConfirmView.as_view(
            template_name="password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        views.PasswordResetCompleteView.as_view(
            template_name="password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path(
        "password_change/",
        views.PasswordChangeView.as_view(template_name="password_change.html"),
        name="password_change",
    ),
    path(
        "password_change/done/",
        views.PasswordChangeDoneView.as_view(
            template_name="password_change_done.html"
        ),
        name="password_change_done",
    ),
]
