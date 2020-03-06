from django.contrib.auth.decorators import permission_required
from django.db.models import Count, Max
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from forum.forms import NewBoardForm
from forum.models import Board, Post, Thread


@require_http_methods(["GET"])
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


@require_http_methods(["GET", "POST"])
def index(request):
    if request.method == "POST":
        return HttpResponse("Not implemented")

    logged_out = request.GET.get("loggedOut")
    boards = __get_boards()
    return render(
        request, "boards/index.html", {"boards": boards, "logged_out": logged_out}
    )


@require_http_methods(["GET"])
def show(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, "boards/show.html", {"board": board})


@require_http_methods(["GET", "POST"])
@permission_required("forum.add_board")
def new(request):
    if request.method == "POST":
        form = NewBoardForm(request.POST)
        if form.is_valid():
            user = request.user
            board = form.save(commit=False)
            board.created_by = user
            board.updated_by = user
            board.save()
            return redirect("boards_show", pk=board.pk)

    form = NewBoardForm()
    return render(request, "boards/new.html", {"form": form})


@require_http_methods(["POST"])
@permission_required("forum.delete_board")
def delete(request, pk):
    board = get_object_or_404(Board, pk=pk)
    board.delete()
    return redirect("boards")
