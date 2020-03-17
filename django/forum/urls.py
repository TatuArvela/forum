from django.shortcuts import redirect
from django.urls import path, re_path
from forum.views import boards, threads, posts

urlpatterns = [
    # Boards
    path("", boards.root_redirect, name="root"),
    re_path(r"^boards/$", boards.index, name="boards"),
    path("boards/<int:pk>/", boards.show, name="boards_show"),
    path("boards/new/", boards.new, name="boards_new"),
    path("boards/delete/<int:pk>/", boards.delete, name="boards_delete"),
    # Threads
    re_path(r"^threads/$", threads.index, name="threads"),
    path("threads/<int:pk>/", threads.show, name="threads_show"),
    re_path(r"^threads/new$", threads.new, name="threads_new"),
    path("threads/delete/<int:pk>/", threads.delete, name="threads_delete"),
    # Posts
    re_path(r"^posts/$", posts.index, name="posts"),
    path("posts/<int:pk>/", posts.show, name="posts_show"),
    re_path(r"^posts/new$", posts.new, name="posts_new"),
    path("posts/delete/<int:pk>/", posts.delete, name="posts_delete"),
]
