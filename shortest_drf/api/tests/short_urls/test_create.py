from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from shortest_drf.short_urls.models import ShortUrl


class ShortUrlCreateViewTest(APITestCase):

    def setUp(self) -> None:
        self.url: str = reverse("short_url_create_view")

    def test_valid_create(self) -> None:
        params: dict = {
            'url': 'https://www.google.com/',
        }

        response = self.client.post(self.url, params, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        instance: ShortUrl = ShortUrl.objects.get(url=params['url'])
        self.assertIsNotNone(instance)
        self.assertEqual(instance.url, params['url'])
        self.assertIsNotNone(instance.slug)
        response = response.json()
        self.assertEqual(response['url'], params['url'])
        self.assertEqual(response['short_url'], f'http://testserver/api/v1/short_urls/{instance.slug}')

    def test_create_without_url_fails(self) -> None:
        response = self.client.post(self.url, {}, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {
            'url': ['This field is required.'],
        })

    def test_create_with_invalid_url_fails(self) -> None:
        invalid_url: str = 'invalid-url'
        response = self.client.post(self.url, {'url': invalid_url}, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {
            'url': [f'Enter a valid URL.'],
        })
