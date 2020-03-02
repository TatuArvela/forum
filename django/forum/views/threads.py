from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import DatabaseError, transaction
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from forum.forms import NewPostForm, NewThreadForm
from forum.models import Board, Post, Thread


def index(request):
    return HttpResponse("Not implemented")


def show(request, pk):
    user = request.user
    thread = get_object_or_404(Thread, pk=pk)

    form = NewPostForm()
    return render(request, "threads/show.html", {"thread": thread, "form": form})


@login_required
def new(request):
    board_pk = request.GET["board_id"]
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
            messages.error(request, "Error")

    form = NewThreadForm(initial={"board": board.pk})
    return render(request, "threads/new.html", {"board": board, "form": form})
