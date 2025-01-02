"""
URL configuration for django_boards project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path

from accounts import views as accounts_views
from boards import views

from django.contrib.auth import views as auth_views

from django.conf import settings
from django_boards.settings import development, base, production
from django.conf.urls.static import static, serve
from django.contrib import admin

urlpatterns = [
    path("", views.BoardListView.as_view(), name="index"),
    path('', include('accounts.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
    path("boards/<pk>/", views.TopicListView.as_view(), name="board_topics"),
    path("boards/<pk>/new/", views.new_topic, name="new_topic"),
    path("boards/<pk>/topics/<topic_pk>/", views.PostListView.as_view(), name="topic_posts"),
    path("boards/<pk>/topics/<topic_pk>/reply/", views.reply_topic, name="reply_topic"),
    path(
        "boards/<pk>/topics/<topic_pk>/posts/<post_pk>/edit/",
        views.PostUpdateView.as_view(),
        name="edit_post",
    ),
    path(
        "boards/<pk>/topics/<topic_pk>/posts/<post_pk>/detail/",
        views.PostDetailView.as_view(),
        name="post_detail",
    ),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path(
        "boards/<pk>/topics/<topic_pk>/posts/<post_pk>/delete/",
        views.PostDeleteView.as_view(),
        name="delete_post",
    ),
    path('avatar/', include('avatar.urls')),
    path('admin/', admin.site.urls),
    # must be commented out in development
    re_path(r'^media/(?P<path>.*\.jpg|.*\.jpeg|.*\.png|.*\.gif)$', serve, {'document_root': production.MEDIA_ROOT}),
] 
if development:
    urlpatterns += static(base.MEDIA_URL, document_root=development.MEDIA_ROOT)