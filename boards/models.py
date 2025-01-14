import math

import nh3
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe
from django.utils.text import Truncator
from markdown import markdown

# Create your models here.


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_posts_count(self):
        return Post.objects.filter(topic__board=self).count()

    def get_latest_post(self):
        return Post.objects.filter(topic__board=self).order_by("-created_at").first()


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="topics")
    starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="topics")
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.subject

    def get_page_count(self):
        count = self.posts.count()
        pages = count / 10
        return math.ceil(pages)

    def has_many_pages(self, count=None):
        if count is None:
            count = self.get_page_count()
        return count > 6

    def get_page_range(self):
        count = self.get_page_count()
        if self.has_many_pages(count):
            return range(1, 5)
        return range(1, count + 1)

    def get_last_ten_posts(self):
        return self.posts.order_by("-created_at")[:10]


class Post(models.Model):
    message = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="+"
    )
    likes = models.ManyToManyField(User, related_name="liked_posts", blank=True)

    def __str__(self):
        # truncated_message = Truncator(self.message)
        # return truncated_message.chars(30)
        return self.message

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

    def get_message_as_markdown(self):
        clean_content = nh3.clean(
            self.message,
            tags={
                "a",
                "abbr",
                "acronym",
                "b",
                "blockquote",
                "code",
                "em",
                "i",
                "li",
                "ol",
                "strong",
                "ul",
                "s",
                "sup",
                "sub",
            },
            attributes={
                "a": {"href"},
                "abbr": {"title"},
                "acronym": {"title"},
            },
            url_schemes={"https"},
            link_rel=None,
        )
        rendered_content = markdown(
            clean_content, extensions=["fenced_code", "codehilite"]
        )
        return mark_safe(rendered_content)
