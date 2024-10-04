from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.utils import timezone
from django.utils.decorators import method_decorator
from .forms import NewTopicForm
from .forms import PostForm
from .models import Board, Topic, Post

# Create your views here.
@method_decorator(login_required, name='dispatch')
class PostDetailView(DetailView):
    model = Post
    fields = ('message', )
    template_name = 'post_detail.html'
    pk_url_kwarg = 'post_pk'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        # total_likes = stuff.total_likes()
        # context['total_likes'] = total_likes
        # context["now"] = timezone.now()
        return context
    

class BoardListView(ListView):
    model = Board
    context_object_name = 'boards'
    template_name = 'index.html'

def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    board = get_object_or_404(Board, pk=pk)
    queryset = board.topics.order_by('-last_updated').annotate(replies=Count('posts') - 1)
    page = request.GET.get('page', 1)

    paginator = Paginator(queryset, 20)

    try:
        topics = paginator.page(page)
    except PageNotAnInteger:
        # fallback to the first page
        topics = paginator.page(1)
    except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
        topics = paginator.page(paginator.num_pages)

    return render(request, "topics.html", {"board": board, 'topics': topics})

@login_required
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = request.user
            topic.save()
            Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=request.user
            )
            # redirect to topic_posts view
            return redirect('topic_posts', pk=pk, topic_pk=topic.pk)
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})

def topic_posts(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    topic.views += 1
    topic.save()
    return render(request, 'topic_posts.html', {'topic': topic})

@login_required
def reply_topic(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
        return redirect('topic_posts', pk=pk, topic_pk=topic_pk)
    else:
        form = PostForm()
    return render(request, 'reply_topic.html', {'topic': topic, 'form': form})

@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
    model = Post
    fields = ('message', )
    template_name = 'edit_post.html'
    pk_url_kwarg = 'post_pk'
    context_object_name = 'post'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(created_by=self.request.user)

    def form_valid(self, form):
        post = form.save(commit=False)
        post.updated_by = self.request.user
        post.updated_at = timezone.now()
        post.save()
        return redirect('topic_posts', pk=post.topic.board.pk, topic_pk=post.topic.pk)

@method_decorator(login_required, name='dispatch')
class PostDeleteView(DeleteView):

    # just as for PostUpdateView, this makes sure the UnauthorizedPostDeleteViewTests status_code test passes, making sure that if the user trying to delete the post does not equal the owner of the post (set here via filter), then they cannot delete the post, and a status code of 404 is rendered instead of 200.
    def get_queryset(self): # added
        queryset = super().get_queryset()
        return queryset.filter(created_by=self.request.user)

    model = Post
    template_name = "post_confirm_delete.html"
    pk_url_kwarg = "post_pk"
    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url = "/"


