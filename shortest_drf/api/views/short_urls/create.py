from typing import Type

from django.db.models import QuerySet
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, BasePermission

from shortest_drf.api.serializers.short_url import ShortUrlSerializer
from shortest_drf.short_urls.models import ShortUrl


class ShortUrlCreateView(CreateAPIView):
    """
    Create short url entry
    """
    permission_classes: list[BasePermission] = [AllowAny]
    queryset: QuerySet = ShortUrl.objects.all()
    serializer_class: Type[ShortUrlSerializer] = ShortUrlSerializer
