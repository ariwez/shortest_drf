
from django.db import models
from django.utils.crypto import get_random_string


from shortest_drf.short_urls.errors import InvalidSlugGenerationError
from shortest_drf.short_urls.settings import SLUG_LENGTH, SLUG_MAX_RETRIES


class ShortUrl(models.Model):
    url = models.URLField(max_length=256, blank=False)
    slug = models.SlugField(max_length=32, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'Short url: {self.slug} for: {self.url} created at: {self.created_at}'

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    def _get_unique_slug(self) -> str:
        """Generate a random slug and check if it is unique. If not, try again."""
        tries_count: int = 0
        slug: str = self._get_random_string()
        while ShortUrl.objects.filter(slug=slug).exists():
            tries_count += 1
            if tries_count > SLUG_MAX_RETRIES:
                raise InvalidSlugGenerationError(self.url)
            slug = self._get_random_string()
        return slug

    def _get_random_string(self) -> str:
        return get_random_string(length=SLUG_LENGTH)