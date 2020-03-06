from django.contrib.auth.models import User
from django.urls import reverse, resolve
from django.test import TestCase
from ..views.boards import index as index_view
from ..models import Board


class RootRedirectTests(TestCase):
    def setUp(self):
        url = reverse("root")
        self.response = self.client.get(url)

    def test_root_redirect_status_code(self):
        self.assertEquals(self.response.status_code, 302)

    def test_root_redirect_resolves_home(self):
        self.assertRedirects(self.response, "/boards/")


class BoardsIndexTests(TestCase):
    def setUp(self):
        test_user = User.objects.create_user(
            username="john", email="john@doe.com", password="123"
        )
        self.board = Board.objects.create(
            title="Django",
            description="Django board.",
            created_by=test_user,
            updated_by=test_user,
        )
        url = reverse("boards")
        self.response = self.client.get(url)

    def test_index_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_index_url_resolves_index_view(self):
        view = resolve("/boards/")
        self.assertEquals(view.func, index_view)

    def test_index_view_contains_link_to_show_page(self):
        show_url = reverse("boards_show", kwargs={"pk": self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(show_url))

class BoardsShowTests(TestCase):
    def setUp(self):
        test = 1

    def test_todo(self):
        self.assertEquals(1, 1)

class BoardsNewTests(TestCase):
    def setUp(self):
        test = 1

    def test_todo(self):
        self.assertEquals(1, 1)

class BoardsDeleteTests(TestCase):
    def setUp(self):
        test = 1

    def test_todo(self):
        self.assertEquals(1, 1)