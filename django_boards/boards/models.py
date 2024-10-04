from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils.text import Truncator

# Create your models here.


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_posts_count(self):
        return Post.objects.filter(topic__board=self).count()

    def get_latest_post(self): # new
        return Post.objects.filter(topic__board=self).order_by('-created_at').first()


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="topics")
    starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="topics")
    views = models.PositiveIntegerField(default=0)
    

    def __str__(self):
        return self.subject


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="+"
    )
    likes = models.ManyToManyField(User, blank=True, related_name="post_likes")

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)
        # return self.message

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
