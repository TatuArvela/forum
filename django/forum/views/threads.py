from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.db import DatabaseError, transaction
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from forum.forms import NewPostForm, NewThreadForm
from forum.models import Board, Post, Thread


@require_http_methods(["GET"])
def index(request):
    return HttpResponse("Not implemented")


@require_http_methods(["GET"])
def show(request, pk):
    user = request.user
    thread = get_object_or_404(Thread, pk=pk)

    form = NewPostForm()
    return render(request, "threads/show.html", {"thread": thread, "form": form})


@require_http_methods(["GET", "POST"])
@permission_required('forum.add_thread')
def new(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)

    if request.method == "POST":
        form = NewThreadForm(request.POST)
        if form.is_valid():
            user = request.user
            thread = form.save(commit=False)
            thread.board = board
            thread.created_by = user
            thread.updated_by = user

            try:
                with transaction.atomic():
                    thread.save()
                    post = Post.objects.create(
                        message=form.cleaned_data.get("message"),
                        created_by=user,
                        updated_by=user,
                        thread=thread,
                    )
            except DatabaseError:
                messages.error(request, "Error")

            return redirect("threads_show", pk=thread.pk)
    else:
        form = NewThreadForm(initial={"board": board.pk})

    return render(request, "threads/new.html", {"board": board, "form": form})


@require_http_methods(["POST"])
@permission_required("forum.delete_thread")
def delete(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    board = get_object_or_404(Board, pk=thread.board.pk)
    thread.delete()
    return redirect("boards_show", pk=board.pk)
