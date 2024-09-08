from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Board(models.Model):
  name = models.CharField(max_length=30, unique=True)
  description = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class Topic(models.Model):
  subject = models.CharField(max_length=255)
  last_updated = models.DateTimeField(auto_now_add=True)
  board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='topics')
  starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topics')


class Post(models.Model):
  message = models.TextField(max_length=4000)
  topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(null=True)
  created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
  updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')
  post_liked = models.ManyToManyField(User, default=None, blank=True, related_name='post_liked')

  @property
  def post_num_likes(self):
    return self.post_liked.all().count()

POST_LIKE_CHOICES = (
  ('♥️', '♥️'),
  ('♡', '♡'),
)

class PostLike(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  post_like_value = models.CharField(choices=POST_LIKE_CHOICES, default='♥️', max_length=2)

  def __str__(self):
    return str(self.post)
  

