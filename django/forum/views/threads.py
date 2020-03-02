from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count, Max
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewPostForm, NewThreadForm
from .models import Board, Post, Thread


def view(request, pk):
    user = request.user
    thread = get_object_or_404(Thread, pk=pk)
    if request.method == "POST":
        if user.is_authenticated:
            form = NewPostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.thread = thread
                post.created_by = user
                post.save()
                return redirect("thread_replies", pk=thread.pk)
        else:
            return redirect("login")
    else:
        form = NewPostForm()
    return render(request, "replies.html", {"thread": thread, "form": form})


@login_required
def new(request, pk):
    user = request.user
    board = get_object_or_404(Board, pk=pk)
    if user.is_authenticated and request.method == "POST":
        form = NewThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.board = board
            thread.created_by = user
            thread.save()
            post = Post.objects.create(
                message=form.cleaned_data.get("message"), thread=thread, created_by=user
            )
            return redirect("thread_replies", pk=thread.pk)
    else:
        form = NewThreadForm()
    return render(request, "new_thread.html", {"board": board, "form": form})

