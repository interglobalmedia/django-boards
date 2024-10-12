from django.urls import path
from .views import profile, UserUpdateView

urlpatterns = [
    path('account/', UserUpdateView.as_view(), name='my_account'),
    path("profile/", profile, name="users-profile"),
]
