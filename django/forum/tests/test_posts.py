from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse, resolve
from django.test import TestCase
from ..views.posts import (
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

    post_content_type = ContentType.objects.get_for_model(Post)
    add_post_permission = Permission.objects.get(
        content_type=post_content_type, codename="add_post"
    )
    delete_post_permission = Permission.objects.get(
        content_type=post_content_type, codename="delete_post"
    )
    self.admin_user.user_permissions.add(add_post_permission)
    self.admin_user.user_permissions.add(delete_post_permission)


class PostsIndexTests(TestCase):
    def setUp(self):
        setUpSharedUsers(self)

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
        url = reverse("posts_show", kwargs={"pk": self.post.pk})
        self.response = self.client.get(url)

    def test_show_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_show_view_response(self):
        self.assertEquals(self.response.content, b"Not implemented")

    def test_show_url_resolves_show_view(self):
        view = resolve("/posts/{0}/".format(self.post.pk))
        self.assertEquals(view.func, show_view)


class PostsNewTests(TestCase):
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

    def test_new_url_resolves_new_view(self):
        view = resolve("/posts/new/{0}/".format(self.thread.pk))
        self.assertEquals(view.func, new_view)

    # TODO: Test that GET is not permitted
    # TODO: Test that reply creation works when authorized
    # TODO: Test that reply creation does not work when not authorized
    # TODO: Test that reply creation does not work when thread with id does not exist
    # TODO: Test behavior when reply form is invalid


class PostsDeleteTests(TestCase):
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
        view = resolve("/posts/{0}/delete/".format(self.post.pk))
        self.assertEquals(view.func, delete_view)

    # TODO: Test that deletion works when authorized
    # TODO: Test that deletion does not work when not authorized
    # TODO: Test behavior when post with id does not exist
