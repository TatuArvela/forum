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
from ..models import Board, Thread, Post


def setUpSharedUsers(self):
    self.basic_user = User.objects.create_user(
        username="john", email="john@doe.com", password="123"
    )
    self.admin_user = User.objects.create_user(
        username="admin", email="admin@admin.com", password="admin"
    )

    board_content_type = ContentType.objects.get_for_model(Board)
    add_board_permission = Permission.objects.get(
        content_type=board_content_type, codename="add_board"
    )
    delete_board_permission = Permission.objects.get(
        content_type=board_content_type, codename="delete_board"
    )
    self.admin_user.user_permissions.add(add_board_permission)
    self.admin_user.user_permissions.add(delete_board_permission)




class RootRedirectTests(TestCase):
    def setUp(self):
        setUpSharedUsers(self)
        url = reverse("root")
        self.response = self.client.get(url)

    def test_root_redirect_status_code(self):
        self.assertEquals(self.response.status_code, 302)

    def test_root_redirect_resolves_home(self):
        self.assertRedirects(self.response, "/boards/")


class BoardsIndexTests(TestCase):
    def setUp(self):
        setUpSharedUsers(self)

        self.board1 = Board.objects.create(
            title="Django",
            description="Discussion regarding development of web apps with Django",
            created_by=self.admin_user,
            updated_by=self.admin_user,
        )
        self.board2 = Board.objects.create(
            title="Python",
            description="General discussion regarding the Python programming language",
            created_by=self.admin_user,
            updated_by=self.admin_user,
        )

        url = reverse("boards")
        self.response = self.client.get(url)

    def test_index_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_index_url_resolves_index_view(self):
        view = resolve("/boards/")
        self.assertEquals(view.func, index_view)

    def test_index_view_contains_links_to_show_view(self):
        board1_show_url = reverse("boards_show", kwargs={"pk": self.board1.pk})
        board2_show_url = reverse("boards_show", kwargs={"pk": self.board2.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board1_show_url))
        self.assertContains(self.response, 'href="{0}"'.format(board2_show_url))

    def test_index_view_contains_board_titles_and_descriptions(self):
        self.assertContains(self.response, self.board1.title)
        self.assertContains(self.response, self.board1.description)
        self.assertContains(self.response, self.board2.title)
        self.assertContains(self.response, self.board2.description)

    # Test length of board table


class BoardsShowTests(TestCase):
    def setUp(self):
        setUpSharedUsers(self)

        self.board = Board.objects.create(
            title="Django Board",
            description="Test description",
            created_by=self.basic_user,
            updated_by=self.basic_user,
        )
        self.thread = Thread.objects.create(
            title="How to test Django apps?",
            board=self.board,
            created_by=self.basic_user,
            updated_by=self.basic_user,
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

    def test_show_board_view_contains_link_back_to_boards(self):
        show_thread_url = reverse("threads_show", kwargs={"pk": 1})
        response = self.client.get(show_thread_url)
        boards_url = reverse("boards")
        self.assertContains(response, 'href="{0}"'.format(boards_url))

    def test_show_board_view_contains_navigation_links_logged_out(self):
        show_thread_url = reverse("threads_show", kwargs={"pk": 1})
        homepage_url = reverse("boards")
        threads_new_url = reverse("threads_new")
        threads_query_string = "?board_id={0}".format(self.board.pk)

        response = self.client.get(show_thread_url)

        self.assertContains(response, 'href="{0}"'.format(homepage_url))
        self.assertNotContains(response, 'href="{0}"'.format(threads_new_url + threads_query_string))

    # def test_show_board_view_contains_navigation_links_logged_in(self):
    #     show_thread_url = reverse("threads_show", kwargs={"pk": 1})
    #     homepage_url = reverse("boards")
    #     threads_new_url = reverse("threads_new")
    #     threads_query_string = "?board_id={0}".format(self.board.pk)

    #     response = self.client.get(show_thread_url)

    #     self.assertContains(response, 'href="{0}"'.format(homepage_url))
    #     self.assertContains(response, 'href="{0}"'.format(threads_new_url + threads_query_string))


class BoardsNewTests(TestCase):
    def setUp(self):
        setUpSharedUsers(self)

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
        setUpSharedUsers(self)

        self.board = Board.objects.create(
            title="Django Board",
            description="Test description",
            created_by=self.basic_user,
            updated_by=self.basic_user,
        )
        self.thread = Thread.objects.create(
            title="How to test Django apps?",
            board=self.board,
            created_by=self.basic_user,
            updated_by=self.basic_user,
        )
        self.post = Post.objects.create(
            message="Please delete this post",
            thread=self.thread,
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
