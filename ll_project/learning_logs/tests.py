from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Entry, Topic


class LearningLogsViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="alice", password="test-pass-123")
        self.other_user = User.objects.create_user(
            username="bob", password="test-pass-123"
        )
        self.topic = Topic.objects.create(text="Python", owner=self.user)

    def test_topics_requires_login(self):
        response = self.client.get(reverse("learning_logs:topics"))

        self.assertRedirects(
            response, f"/accounts/login/?next={reverse('learning_logs:topics')}"
        )

    def test_owner_can_create_topic(self):
        self.client.login(username="alice", password="test-pass-123")

        response = self.client.post(
            reverse("learning_logs:new_topic"), {"text": "Django"}
        )

        self.assertRedirects(response, reverse("learning_logs:topics"))
        self.assertTrue(Topic.objects.filter(text="Django", owner=self.user).exists())

    def test_owner_can_create_entry(self):
        self.client.login(username="alice", password="test-pass-123")

        response = self.client.post(
            reverse("learning_logs:new_entry", args=[self.topic.id]),
            {"text": "Use the Django test client."},
        )

        self.assertRedirects(
            response, reverse("learning_logs:topic", args=[self.topic.id])
        )
        self.assertTrue(Entry.objects.filter(topic=self.topic).exists())

    def test_user_cannot_create_entry_for_another_users_topic(self):
        self.client.login(username="bob", password="test-pass-123")

        response = self.client.post(
            reverse("learning_logs:new_entry", args=[self.topic.id]),
            {"text": "This must not be saved."},
        )

        self.assertEqual(response.status_code, 404)
        self.assertFalse(Entry.objects.filter(topic=self.topic).exists())
