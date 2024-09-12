from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from .models import Board

# Create your views here.
def index(request):
  boards = Board.objects.all()
  return render(request, 'index.html', {'boards': boards})

def board_topics(request, id):
  board = get_object_or_404(Board, id=id)
  return render(request, 'topics.html', {'board': board})

def new_topic(request, id):
  board = get_object_or_404(Board, id=id)
  return render(request, 'new_topic.html', {'board': board})



