from django.contrib.auth.models import User
from django.urls import reverse, resolve
from django.test import TestCase
from ..views.threads import (
    index as index_view,
    show as show_view,
    new as new_view,
    delete as delete_view,
)
from ..models import Board, Thread


class ThreadsIndexTests(TestCase):
    def setUp(self):
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

    def test_todo(self):
        self.assertEquals(1, 1)


class ThreadsNewTests(TestCase):
    def setUp(self):
        test = 1

    def test_todo(self):
        self.assertEquals(1, 1)


class ThreadsDeleteTests(TestCase):
    def setUp(self):
        test = 1

    def test_todo(self):
        self.assertEquals(1, 1)


# class NewTopicTests(TestCase):
#     def setUp(self):
#         Board.objects.create(name="Django", description="Django board.")
#         User.objects.create_user(username="john", email="john@doe.com", password="123")

#     def test_new_topic_view_success_status_code(self):
#         url = reverse("new_topic", kwargs={"pk": 1})
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 200)

#     def test_new_topic_view_not_found_status_code(self):
#         url = reverse("new_topic", kwargs={"pk": 99})
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 404)

#     def test_new_topic_url_resolves_new_topic_view(self):
#         view = resolve("/boards/1/new/")
#         self.assertEquals(view.func, new_topic)

#     def test_new_topic_view_contains_link_back_to_board_topics_view(self):
#         new_topic_url = reverse("new_topic", kwargs={"pk": 1})
#         board_topics_url = reverse("board_topics", kwargs={"pk": 1})
#         response = self.client.get(new_topic_url)
#         self.assertContains(response, 'href="{0}"'.format(board_topics_url))

#     def test_csrf(self):
#         url = reverse("new_topic", kwargs={"pk": 1})
#         response = self.client.get(url)
#         self.assertContains(response, "csrfmiddlewaretoken")

#     def test_new_topic_valid_post_data(self):
#         url = reverse("new_topic", kwargs={"pk": 1})
#         data = {"subject": "Test title", "message": "Lorem ipsum dolor sit amet"}
#         response = self.client.post(url, data)
#         self.assertTrue(Topic.objects.exists())
#         self.assertTrue(Post.objects.exists())

#     def test_new_topic_invalid_post_data(self):
#         """
#         Invalid post data should not redirect
#         The expected behavior is to show the form again with validation errors
#         """
#         url = reverse("new_topic", kwargs={"pk": 1})
#         response = self.client.post(url, {})
#         self.assertEquals(response.status_code, 200)

#     def test_new_topic_invalid_post_data_empty_fields(self):
#         """
#         Invalid post data should not redirect
#         The expected behavior is to show the form again with validation errors
#         """
#         url = reverse("new_topic", kwargs={"pk": 1})
#         data = {"subject": "", "message": ""}
#         response = self.client.post(url, data)
#         self.assertEquals(response.status_code, 200)
#         self.assertFalse(Topic.objects.exists())
#         self.assertFalse(Post.objects.exists())

#     def test_contains_form(self):  # <- new test
#         url = reverse("new_topic", kwargs={"pk": 1})
#         response = self.client.get(url)
#         form = response.context.get("form")
#         self.assertIsInstance(form, NewTopicForm)

#     def test_new_topic_invalid_post_data(self):  # <- updated this one
#         """
#         Invalid post data should not redirect
#         The expected behavior is to show the form again with validation errors
#         """
#         url = reverse("new_topic", kwargs={"pk": 1})
#         response = self.client.post(url, {})
#         form = response.context.get("form")
#         self.assertEquals(response.status_code, 200)
#         self.assertTrue(form.errors)
