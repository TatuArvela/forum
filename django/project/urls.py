from django.shortcuts import redirect
from django.conf.urls import include
from django.urls import path, re_path
from django.contrib import admin
from forum.views import boards

urlpatterns = [
    path("", boards.index, name="root"),
    # path("", redirect("views.boards"), name="root"),
    # re_path(r"^boards/$", views.boards, name="boards"),
    # path("boards/<int:pk>/", views.board_threads, name="board_threads"),
    # path("boards/<int:pk>/new/", views.new_thread, name="new_thread"),
    # path("threads/<int:pk>/", views.thread_replies, name="thread_replies"),
]

# Add Django site admin urls
urlpatterns += [
    path("admin/", admin.site.urls),
]

# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path("accounts/", include("django.contrib.auth.urls")),
]
