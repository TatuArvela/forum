from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from django.urls import reverse, resolve
from ..views.boards import (
    index as index_view,
    show as show_view,
    new as new_view,
    delete as delete_view,
)
from ..models import Board, Thread


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
        self.user = User.objects.create_user(
            username="john", email="john@doe.com", password="123"
        )
        self.board = Board.objects.create(
            title="Django",
            description="Django board.",
            created_by=self.user,
            updated_by=self.user,
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
        self.user = User.objects.create_user(
            username="john", email="john@doe.com", password="123"
        )
        self.board = Board.objects.create(
            title="Django",
            description="Django board.",
            created_by=self.user,
            updated_by=self.user,
        )
        self.thread = Thread.objects.create(
            title="How to test Django apps?",
            board=self.board,
            created_by=self.user,
            updated_by=self.user,
        )
        url = reverse("boards_show", kwargs={"pk": self.board.pk})
        self.response = self.client.get(url)

    def test_show_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_non_existent_board_not_found(self):
        url = reverse("boards_show", kwargs={"pk": 2})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_show_url_resolves_show_view(self):
        view = resolve("/boards/{0}/".format(self.board.pk))
        self.assertEquals(view.func, show_view)

    def test_show_board_view_contains_link_to_show_thread_page(self):
        show_thread_url = reverse("threads_show", kwargs={"pk": self.thread.pk})
        self.assertContains(self.response, 'href="{0}"'.format(show_thread_url))


class BoardsNewTests(TestCase):
    def setUp(self):
        self.basic_user = User.objects.create_user(
            username="john", email="john@doe.com", password="123"
        )
        self.admin_user = User.objects.create_user(
            username="admin", email="admin@admin.com", password="admin"
        )

        content_type = ContentType.objects.get_for_model(Board)
        permission = Permission.objects.get(
            content_type=content_type, codename="add_board"
        )

        self.admin_user.user_permissions.add(permission)

        self.board = Board.objects.create(
            title="Django",
            description="Django board.",
            created_by=self.basic_user,
            updated_by=self.basic_user,
        )

    def test_new_view_status_code_as_not_permitted_user(self):
        self.client.force_login(self.basic_user)
        url = reverse("boards_new")
        self.response = self.client.get(url)
        self.assertEquals(self.response.status_code, 302)

    def test_new_view_status_code_as_permitted_user(self):
        self.client.force_login(self.admin_user)
        url = reverse("boards_new")
        self.response = self.client.get(url)
        self.assertEquals(self.response.status_code, 200)

    def test_new_url_resolves_new_view(self):
        view = resolve("/boards/new/")
        self.assertEquals(view.func, new_view)


class BoardsDeleteTests(TestCase):
    def setUp(self):
        self.basic_user = User.objects.create_user(
            username="john", email="john@doe.com", password="123"
        )
        self.admin_user = User.objects.create_user(
            username="admin", email="admin@admin.com", password="admin"
        )

        content_type = ContentType.objects.get_for_model(Board)
        permission = Permission.objects.get(
            content_type=content_type, codename="delete_board"
        )

        self.admin_user.user_permissions.add(permission)

        self.board = Board.objects.create(
            title="Django",
            description="Django board.",
            created_by=self.basic_user,
            updated_by=self.basic_user,
        )

    # TODO: Figure out a way to test these properly

    # def test_new_view_status_code_as_not_permitted_user(self):
    #     self.client.force_login(self.basic_user)
    #     url = reverse("boards_delete", kwargs={"pk": self.board.pk})
    #     self.response = self.client.post(url, follow=True)
    #     self.assertEquals(self.response.status_code, 302)

    # def test_new_view_status_code_as_permitted_user(self):
    #     self.client.force_login(self.admin_user)
    #     url = reverse("boards_delete", kwargs={"pk": self.board.pk})
    #     self.response = self.client.post(url, follow=True)
    #     self.assertEquals(self.response.status_code, 200)

    # def test_new_view_status_code_as_permitted_user_nonexistent_board(self):
    #     self.client.force_login(self.admin_user)
    #     url = reverse("boards_delete", kwargs={"pk": 2})
    #     self.response = self.client.post(url, follow=True)
    #     self.assertEquals(self.response.status_code, 404)

    def test_new_url_resolves_new_view(self):
        view = resolve("/boards/delete/{0}/".format(self.board.pk))
        self.assertEquals(view.func, delete_view)
