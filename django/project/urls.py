from django.conf.urls import include
from django.urls import path, re_path
from django.contrib import admin
from boards import views

urlpatterns = [
    path("", views.root, name="root"),
    re_path(r"^boards/$", views.boards, name="boards"),
    path("boards/<int:pk>/", views.board_topics, name="board_topics"),
    path("boards/<int:pk>/new/", views.new_topic, name="new_topic"),
    path("topics/<int:pk>/", views.topic_replies, name="topic_replies"),
]

# Add Django site admin urls
urlpatterns += [
    path("admin/", admin.site.urls),
]

# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path("accounts/", include("django.contrib.auth.urls")),
]
