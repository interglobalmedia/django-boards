from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import NewTopicForm
from .forms import PostForm
from .models import Board, Topic, Post

# Create your views here.
def index(request):
    boards = Board.objects.all()
    return render(request, "index.html", {"boards": boards})


def board_topics(request, id):
    board = get_object_or_404(Board, id=id)
    topics = board.topics.order_by('-last_updated').annotate(replies=Count('posts') - 1)
    return render(request, "topics.html", {"board": board, 'topics': topics})

@login_required
def new_topic(request, id):
    board = get_object_or_404(Board, id=id)
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = request.user  # <- here
            topic.save()
            Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=request.user  # <- and here
            )
            return redirect('topic_posts', id=id, topic_id=topic.id)  # redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})

def topic_posts(request, id, topic_id):
    topic = get_object_or_404(Topic, board__id=id, id=topic_id)
    topic.views += 1
    topic.save()
    return render(request, 'topic_posts.html', {'topic': topic})

@login_required
def reply_topic(request, id, topic_id):
    topic = get_object_or_404(Topic, board__id=id, id=topic_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('topic_posts', id=id, topic_id=topic_id)
    else:
        form = PostForm()
    return render(request, 'reply_topic.html', {'topic': topic, 'form': form})

