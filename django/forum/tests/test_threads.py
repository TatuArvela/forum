from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse, resolve
from django.test import TestCase
from ..views.threads import (
    index as index_view,
    show as show_view,
    new as new_view,
    delete as delete_view,
)
from ..models import Board, Thread, Post
from ..forms import NewThreadForm


def setUpSharedUsers(self):
    self.basic_user = User.objects.create_user(
        username="john", email="john@doe.com", password="123"
    )
    self.admin_user = User.objects.create_user(
        username="admin", email="admin@admin.com", password="admin"
    )

    thread_content_type = ContentType.objects.get_for_model(Thread)
    add_thread_permission = Permission.objects.get(
        content_type=thread_content_type, codename="add_thread"
    )
    delete_thread_permission = Permission.objects.get(
        content_type=thread_content_type, codename="delete_thread"
    )
    self.admin_user.user_permissions.add(add_thread_permission)
    self.admin_user.user_permissions.add(delete_thread_permission)


class ThreadsIndexTests(TestCase):
    def setUp(self):
        setUpSharedUsers(self)

        url = reverse("threads")
        self.response = self.client.get(url)

    def test_index_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_index_view_response(self):
        self.assertEquals(self.response.content, b"Not implemented")

    def test_index_url_resolves_index_view(self):
        view = resolve("/threads/")
        self.assertEquals(view.func, index_view)


class ThreadsShowTests(TestCase):
    def setUp(self):
        setUpSharedUsers(self)

        self.board = Board.objects.create(
            title="Django",
            description="Django board.",
            created_by=self.admin_user,
            updated_by=self.admin_user,
        )
        self.thread = Thread.objects.create(
            title="How to test Django apps?",
            board=self.board,
            created_by=self.basic_user,
            updated_by=self.basic_user,
        )
        self.post = Post.objects.create(
            message="I don't know how to make proper tests for Django apps",
            thread=self.thread,
            created_by=self.basic_user,
            updated_by=self.basic_user,
        )

        url = reverse("threads_show", kwargs={"pk": self.thread.pk})
        self.response = self.client.get(url)

    def test_show_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_non_existent_thread_not_found(self):
        url = reverse("threads_show", kwargs={"pk": 2})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_show_url_resolves_show_view(self):
        view = resolve("/threads/{0}/".format(self.thread.pk))
        self.assertEquals(view.func, show_view)

    def test_show_thread_view_contains_link_back_to_boards(self):
        show_threads_url = reverse("threads_show", kwargs={"pk": 1})
        response = self.client.get(show_threads_url)
        boards_url = reverse("boards")
        self.assertContains(response, 'href="{0}"'.format(boards_url))

    def test_show_thread_view_contains_link_back_to_parent_board(self):
        show_threads_url = reverse("threads_show", kwargs={"pk": 1})
        response = self.client.get(show_threads_url)
        show_boards_url = reverse("boards_show", kwargs={"pk": 1})
        self.assertContains(response, 'href="{0}"'.format(show_boards_url))

    # TODO: Test the amount of replies in the thread
    # TODO: Test the visibility of the "Delete" button
    # TODO: Test the visibility of the "Reply to thread" form


class ThreadsNewTests(TestCase):
    def setUp(self):
        setUpSharedUsers(self)

        self.board = Board.objects.create(
            title="Django Board",
            description="Test description",
            created_by=self.basic_user,
            updated_by=self.basic_user,
        )

    def test_new_url_resolves_new_view(self):
        self.client.force_login(self.admin_user)
        view = resolve("/threads/new/{0}/".format(self.board.pk))
        self.assertEquals(view.func, new_view)

    def test_new_view_success_status_code(self):
        self.client.force_login(self.admin_user)
        url = reverse("threads_new", kwargs={"board_pk": self.board.pk})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_new_view_not_found_status_code(self):
        self.client.force_login(self.admin_user)
        url = reverse("threads_new", kwargs={"board_pk": 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_new_view_contains_link_back_to_board(self):
        self.client.force_login(self.admin_user)
        new_url = reverse("threads_new", kwargs={"board_pk": 1})
        boards_show_url = reverse("boards_show", kwargs={"pk": 1})
        response = self.client.get(new_url)
        self.assertContains(response, 'href="{0}"'.format(boards_show_url))

    def test_csrf(self):
        self.client.force_login(self.admin_user)
        url = reverse("threads_new", kwargs={"board_pk": 1})
        response = self.client.get(url)
        self.assertContains(response, "csrfmiddlewaretoken")

    def test_new_valid_post_data(self):
        self.client.force_login(self.admin_user)
        url = reverse("threads_new", kwargs={"board_pk": 1})
        data = {"title": "Test title", "message": "Lorem ipsum dolor sit amet"}
        response = self.client.post(url, data)
        self.assertTrue(Thread.objects.exists())
        self.assertTrue(Post.objects.exists())

    def test_new_invalid_post_data(self):
        self.client.force_login(self.admin_user)
        url = reverse("threads_new", kwargs={"board_pk": 1})
        response = self.client.post(url, {})
        form = response.context.get("form")
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)

    def test_new_invalid_post_data_empty_fields(self):
        self.client.force_login(self.admin_user)
        url = reverse("threads_new", kwargs={"board_pk": 1})
        data = {"subject": "", "message": ""}
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertFalse(Thread.objects.exists())
        self.assertFalse(Post.objects.exists())

    def test_contains_form(self):
        self.client.force_login(self.admin_user)
        url = reverse("threads_new", kwargs={"board_pk": 1})
        response = self.client.get(url)
        form = response.context.get("form")
        self.assertIsInstance(form, NewThreadForm)


    # TODO: Test that thread creation does not work when not authorized
    # TODO: Test that thread creation does not work when board with id does not exist


class ThreadsDeleteTests(TestCase):
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

    def test_delete_url_resolves_delete_view(self):
        view = resolve("/threads/{0}/delete/".format(self.post.pk))
        self.assertEquals(view.func, delete_view)

    # TODO: Test that deletion works when authorized
    # TODO: Test that deletion does not work when not authorized
    # TODO: Test behavior when thread with id does not exist
