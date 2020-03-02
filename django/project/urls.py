from django.shortcuts import redirect
from django.conf.urls import include
from django.urls import path, re_path
from django.contrib import admin
from forum.views import boards, threads, posts

urlpatterns = [
    path("", boards.root_redirect, name="root"),
    re_path(r"^boards/$", boards.index, name="boards"),
    path("boards/<int:pk>/", boards.show, name="boards_show"),
    re_path(r"^boards/new$", boards.new, name="boards_new"),
    re_path(r"^threads/$", threads.index, name="threads"),
    path("threads/<int:pk>/", threads.show, name="threads_show"),
    re_path(r"^threads/new$", threads.new, name="threads_new"),
    re_path(r"^posts/$", posts.index, name="posts"),
    path("posts/<int:pk>/", posts.show, name="posts_show"),
    re_path(r"^posts/new$", posts.new, name="posts_new"),
    # Add Django site admin urls
    path("admin/", admin.site.urls),
    # Add Django site authentication urls (for login, logout, password management)
    path("accounts/", include("django.contrib.auth.urls")),
]
