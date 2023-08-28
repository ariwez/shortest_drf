from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from shortest_drf.short_urls.models import ShortUrl


class ShortUrlRetrieveViewTest(APITestCase):

    def test_retrieving_short_url_success(self) -> None:
        url: str = 'https://www.google.com/'
        short_url: ShortUrl = ShortUrl.objects.create(url=url)
        self.assertIsNotNone(short_url)

        api_url: str = reverse("short_url_retrieve_view", kwargs={'slug': short_url.slug})
        response = self.client.get(api_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['url'], url)

    def test_retrieving_short_url_with_invalid_slug_fails(self) -> None:
        invalid_slug: str = 'invalid-slug'
        api_url: str = reverse("short_url_retrieve_view", kwargs={'slug': invalid_slug})
        response = self.client.get(api_url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {
            'detail': 'Not found.'
        })
