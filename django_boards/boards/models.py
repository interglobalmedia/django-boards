from django.db import models
from django.contrib.auth.models import User
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
    post_liked_by = models.ManyToManyField(
        User, default=None, blank=True, related_name="post_like"
    )

    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)
        # return self.message

    @property
    def post_num_likes(self):
        return self.post_liked_by.all().count()

POST_LIKE_CHOICES = (
    ("♥️", "♥️"),
    ("♡", "♡"),
)


class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    post_like_value = models.CharField(
        choices=POST_LIKE_CHOICES, default="♥️", max_length=2
    )

    def __str__(self):
        return str(self.post)
