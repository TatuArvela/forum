from django.conf.urls import include
from django.urls import path, re_path
from django.contrib import admin

urlpatterns = [
    # Add Forum urls
    re_path(r"^", include("forum.urls")),
    # Add Django site admin urls
    path("admin/", admin.site.urls),
    # Add Django site authentication urls (for login, logout, password management)
    path("accounts/", include("django.contrib.auth.urls")),
]
