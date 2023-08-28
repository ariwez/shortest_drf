from typing import Type

from django.db.models import QuerySet
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny, BasePermission

from shortest_drf.api.serializers.url import UrlSerializer
from shortest_drf.short_urls.models import ShortUrl


class ShortUrlRetrieveView(RetrieveAPIView):
    """
    Get url by slug
    """
    permission_classes: list[BasePermission] = [AllowAny]
    queryset: QuerySet = ShortUrl.objects.all()
    serializer_class: Type[UrlSerializer] = UrlSerializer
    lookup_field = 'slug'

