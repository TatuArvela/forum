from django.contrib.auth.models import User
from django.urls import reverse, resolve
from django.test import TestCase
from ..views.posts import (
    index as index_view,
    show as show_view,
    new as new_view,
    delete as delete_view,
)
from ..models import Board, Thread, Post


class PostsIndexTests(TestCase):
    def setUp(self):
        url = reverse("posts")
        self.response = self.client.get(url)

    def test_index_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_index_view_response(self):
        self.assertEquals(self.response.content, b"Not implemented")

    def test_index_url_resolves_index_view(self):
        view = resolve("/posts/")
        self.assertEquals(view.func, index_view)


class PostsShowTests(TestCase):
    def setUp(self):
        test = 1

    def test_todo(self):
        self.assertEquals(1, 1)


class PostsNewTests(TestCase):
    def setUp(self):
        test = 1

    def test_todo(self):
        self.assertEquals(1, 1)


class PostsDeleteTests(TestCase):
    def setUp(self):
        test = 1

    def test_todo(self):
        self.assertEquals(1, 1)
