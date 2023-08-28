from unittest import mock
from unittest.mock import patch, MagicMock

from django.db import IntegrityError
from django.test import TestCase

from shortest_drf.short_urls.errors import InvalidSlugGenerationError
from shortest_drf.short_urls.models import ShortUrl


class ShortUrlTest(TestCase):

    def test_create(self) -> None:
        parameters: dict = {
            'url': 'https://www.google.com/',
            'slug': 'test-slug',
        }
        short_url: ShortUrl = ShortUrl.objects.create(**parameters)

        self.assertEqual(short_url.url, parameters['url'])
        self.assertEqual(short_url.slug, parameters['slug'])
        self.assertIsNotNone(short_url.created_at)
        self.assertIsNotNone(short_url.updated_at)

    def test_create_without_slug(self) -> None:
        parameters: dict = {
            'url': 'https://www.google.com/',
        }
        short_url: ShortUrl = ShortUrl.objects.create(**parameters)

        self.assertEqual(short_url.url, parameters['url'])
        self.assertIsNotNone(short_url.slug)
        self.assertIsNotNone(short_url.created_at)
        self.assertIsNotNone(short_url.updated_at)

    def test_create_with_existing_slug_fails(self) -> None:
        parameters: dict = {
            'url': 'https://www.google.com/',
            'slug': 'test-slug',
        }
        ShortUrl.objects.create(**parameters)
        with self.assertRaises(IntegrityError):
            ShortUrl.objects.create(**parameters)

    def test_generate_unique_slug_fails_with_error(self) -> None:
        parameters: dict = {
            'url': 'https://www.google.com/',
            'slug': 'test-slug',
        }
        ShortUrl.objects.create(**parameters)

        with mock.patch('shortest_drf.short_urls.models.ShortUrl._get_random_string', return_value='test-slug'):
            with self.assertRaises(InvalidSlugGenerationError):
                ShortUrl.objects.create(url='https://www.example.com')