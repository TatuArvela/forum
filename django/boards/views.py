from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count, Max
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewPostForm, NewTopicForm
from .models import Board, Post, Topic


def root(request):
    response = redirect(boards)
    return response


def boards(request):
    logged_out = request.GET.get("loggedOut")
    boards = []
    for board in Board.objects.all().prefetch_related("topics"):
        display_board = {}
        display_board["pk"] = board.pk
        display_board["name"] = board.name
        display_board["description"] = board.description
        display_board["topic_count"] = board.topics.count
        display_board["post_count"] = board.topics.aggregate(Count("posts"))[
            "posts__count"
        ]
        display_board["last_update"] = board.topics.aggregate(Max("posts__updated_at"))[
            "posts__updated_at__max"
        ]
        boards.append(display_board)
    return render(request, "boards.html", {"boards": boards, "logged_out": logged_out})


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, "topics.html", {"board": board})


@login_required
def new_topic(request, pk):
    user = request.user
    board = get_object_or_404(Board, pk=pk)
    if user.is_authenticated and request.method == "POST":
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.created_by = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get("message"), topic=topic, created_by=user
            )
            return redirect("topic_replies", pk=topic.pk)
    else:
        form = NewTopicForm()
    return render(request, "new_topic.html", {"board": board, "form": form})


def topic_replies(request, pk):
    user = request.user
    topic = get_object_or_404(Topic, pk=pk)
    if request.method == "POST":
        if user.is_authenticated:
            form = NewPostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.topic = topic
                post.created_by = user
                post.save()
                return redirect("topic_replies", pk=topic.pk)
        else:
            return redirect("login")
    else:
        form = NewPostForm()
    return render(request, "replies.html", {"topic": topic, "form": form})
