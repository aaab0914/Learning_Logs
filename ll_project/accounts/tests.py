from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AccountViewTests(TestCase):
    def test_register_creates_and_logs_in_user(self):
        response = self.client.post(
            reverse("accounts:register"),
            {
                "username": "new-user",
                "password1": "safe-test-password-123",
                "password2": "safe-test-password-123",
            },
        )

        self.assertRedirects(response, reverse("learning_logs:index"))
        self.assertTrue(User.objects.filter(username="new-user").exists())
        self.assertEqual(
            str(self.client.session.get("_auth_user_id")),
            str(User.objects.get(username="new-user").id),
        )
