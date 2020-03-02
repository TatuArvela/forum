from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count, Max
from django.shortcuts import render, get_object_or_404, redirect
from forum.forms import NewPostForm, NewThreadForm
from forum.models import Board, Post, Thread


def index(request):
    logged_out = request.GET.get("loggedOut")
    boards = []
    for board in Board.objects.all().prefetch_related("threads"):
        display_board = {}
        display_board["pk"] = board.pk
        display_board["title"] = board.title
        display_board["description"] = board.description
        display_board["thread_count"] = board.threads.count
        display_board["post_count"] = board.threads.aggregate(Count("posts"))[
            "posts__count"
        ]
        display_board["last_update"] = board.threads.aggregate(
            Max("posts__updated_at")
        )["posts__updated_at__max"]
        boards.append(display_board)
    return render(request, "index.html", {"boards": boards, "logged_out": logged_out})


def new(request):
    return HttpResponse("Not implemented")


def view(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, "view.html", {"board": board})

