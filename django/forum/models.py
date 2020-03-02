from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, related_name="created_%(class)ss", on_delete=models.CASCADE
    )
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

    class Meta:
        abstract = True


class Board(BaseModel):
    title = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Thread(BaseModel):
    title = models.CharField(max_length=255)
    board = models.ForeignKey(Board, related_name="threads", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Post(BaseModel):
    message = models.TextField(max_length=4000)
    thread = models.ForeignKey(Thread, related_name="posts", on_delete=models.CASCADE)

    def __str__(self):
        return self.message
