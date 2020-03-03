from django.contrib.auth.decorators import permission_required
from django.db.models import Count, Max
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from forum.models import Board, Post, Thread


def root_redirect(request):
    return redirect("boards")


def __get_boards():
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
    return boards


def index(request):
    if request.method == "GET":
        logged_out = request.GET.get("loggedOut")
        boards = __get_boards()
        return render(
            request, "boards/index.html", {"boards": boards, "logged_out": logged_out}
        )

    elif request.method == "POST":
        return HttpResponse("Not implemented")

    else:
        return HttpResponse("Invalid method")


def show(request, pk):
    if request.method == "GET":
        board = get_object_or_404(Board, pk=pk)
        return render(request, "boards/show.html", {"board": board})

    else:
        return HttpResponse("Invalid method")


@permission_required('forum.add_board')
def new(request):
    if request.method == "GET":
        return HttpResponse("Not implemented")

    else:
        return HttpResponse("Invalid method")

