from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from forum.forms import NewPostForm
from forum.models import Thread


def index(request):
    return HttpResponse("Not implemented")


def show(request):
    return HttpResponse("Not implemented")


@permission_required('forum.add_post')
def new(request):
    thread_pk = request.GET["thread_id"]
    thread = get_object_or_404(Thread, pk=thread_pk)

    if request.method == "POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            user = request.user
            post = form.save(commit=False)
            post.thread = thread
            post.created_by = user
            post.updated_by = user
            post.save()
            return redirect("threads_show", pk=thread.pk)
