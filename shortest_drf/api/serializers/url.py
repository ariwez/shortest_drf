from rest_framework import serializers

from shortest_drf.short_urls.models import ShortUrl


class UrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShortUrl
        fields = ('url',)
        read_only_fields = ('url',)
