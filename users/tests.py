from django.test import TestCase
from http import HTTPStatus
from django.urls import reverse


class UserRegistrationViewTest(TestCase):
    def setUp(self):
        self.path = reverse("users:register")

    def test_user_ragistration_get(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "users/register.html")
