from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    board = models.ForeignKey(Board, related_name="topics", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name="topics", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.subject


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name="posts", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name="created_posts", on_delete=models.CASCADE
    )
    updated_at = models.DateTimeField(auto_now_add=True)
    edited_by = models.ForeignKey(
        User, related_name="edited_posts", null=True, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.message

