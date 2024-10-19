from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import ShortenedURL


class URLShortenTests(APITestCase):

    def setUp(self):
        self.valid_url = "https://www.example.com"
        self.invalid_url = "www.example.com"
        self.url = reverse("shorten-url")

    def test_shorten_url_valid(self) -> None:
        response = self.client.post(self.url, {"original_url": self.valid_url})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("short_code", response.data)

    def test_shorten_url_invalid(self):
        response = self.client.post(self.url, {"original_url": self.invalid_url})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_redirect_url_valid(self):
        ShortenedURL.objects.create(original_url=self.valid_url, short_code="abc123")
        redirect_url_endpoint = reverse("redirect-url", kwargs={"short_code": "abc123"})

        response = self.client.get(redirect_url_endpoint)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertRedirects(response, self.valid_url, fetch_redirect_response=False)

    def test_redirect_url_invalid(self):
        redirect_url_endpoint = reverse(
            "redirect-url", kwargs={"short_code": "invalid_code"}
        )
        response = self.client.get(redirect_url_endpoint)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
