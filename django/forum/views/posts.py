from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from forum.forms import NewPostForm
from forum.models import Post, Thread


@require_http_methods(["GET"])
def index(request):
    return HttpResponse("Not implemented")


@require_http_methods(["GET"])
def show(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return HttpResponse("Not implemented")


@require_http_methods(["POST"])
@permission_required("forum.add_post")
def new(request, thread_pk):
    thread = get_object_or_404(Thread, pk=thread_pk)

    form = NewPostForm(request.POST)
    if form.is_valid():
        user = request.user
        post = form.save(commit=False)
        post.thread = thread
        post.created_by = user
        post.updated_by = user
        post.save()
        return redirect("threads_show", pk=thread.pk)


@require_http_methods(["POST"])
@permission_required("forum.delete_post")
def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    thread = get_object_or_404(Thread, pk=post.thread.pk)
    post.delete()
    return redirect("threads_show", pk=thread.pk)
