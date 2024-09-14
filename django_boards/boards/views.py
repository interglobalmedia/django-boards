from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import NewTopicForm
from .models import Board, Topic, Post


# Create your views here.
def index(request):
    boards = Board.objects.all()
    return render(request, "index.html", {"boards": boards})


def board_topics(request, id):
    board = get_object_or_404(Board, id=id)
    return render(request, "topics.html", {"board": board})


def new_topic(request, id):
    board = get_object_or_404(Board, id=id)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('board_topics', id=board.id)  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})
