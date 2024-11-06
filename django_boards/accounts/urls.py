from django.urls import path
from .views import profile, profile_detail, ProfileListView, UserUpdateView

urlpatterns = [
    path('account/', UserUpdateView.as_view(), name='my_account'),
    path("profile/", profile, name="users-profile"),
    path('profile-detail/<int:pk>/', profile_detail, name='profile'),
    path("profiles/", ProfileListView.as_view(), name="users-profile-list"),
]
