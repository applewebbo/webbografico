from unittest.mock import patch

from django.contrib.messages import get_messages
from django.core import mail
from django.urls import reverse
from django_recaptcha.client import RecaptchaResponse

from core.test import TestCase


class IndexView(TestCase):
    def test_get(self):
        response = self.get("index")

        self.response_200(response)
        self.assertTemplateUsed(response, "core/index.html")


class ContactViewTest(TestCase):
    def setUp(self):
        self.valid_data = {
            "name": "John Doe",
            "email": "john@example.com",
            "message": "Test message",
        }

    def test_get_contact_page(self):
        response = self.get("contact")
        self.response_200(response)
        self.assertTemplateUsed(response, "core/contact.html")

    @patch("django_recaptcha.client.submit")
    def test_post_valid_form(self, mocked_submit):
        mocked_submit.return_value = RecaptchaResponse(
            is_valid=True, extra_data={"score": "1"}
        )
        self.valid_data["captcha"] = "PASSED"
        response = self.post("contact", data=self.valid_data)
        self.assertRedirects(response, reverse("index"))
        message = list(get_messages(response.wsgi_request))[0].message
        assert message == "Messaggio inviato con successo"

    @patch("django_recaptcha.client.submit")
    def test_post_invalid_form(self, mocked_submit):
        mocked_submit.return_value = RecaptchaResponse(
            is_valid=True, extra_data={"score": "1"}
        )
        invalid_data = self.valid_data.copy()
        invalid_data["captcha"] = "PASSED"
        invalid_data["email"] = "invalid_email"
        response = self.post("contact", data=invalid_data)
        self.response_200(response)
        self.assertTemplateUsed(response, "core/contact.html")
        self.assertIn("Enter a valid email address", response.content.decode())

    @patch("django_recaptcha.client.submit")
    def test_send_mail_called(self, mocked_submit):
        mocked_submit.return_value = RecaptchaResponse(
            is_valid=True, extra_data={"score": "1"}
        )
        self.valid_data["captcha"] = "PASSED"
        self.post("contact", data=self.valid_data)
        self.assertEqual(len(mail.outbox), 1)
        sent_mail = mail.outbox[0]
        self.assertEqual(sent_mail.subject, "Contatto da John Doe su webbografico.com")
        self.assertIn("Test message", sent_mail.body)
        self.assertIn("john@example.com", sent_mail.body)

    def test_context_data(self):
        response = self.get("contact")
        self.assertIn("form", response.context)
        self.assertTrue(response.context["create"])

    def test_empty_form_submission(self):
        response = self.post("contact", data={})
        self.response_200(response)
        assert "form" in response.context
