from rest_framework import serializers

from shortest_drf.short_urls.models import ShortUrl


class ShortUrlSerializer(serializers.ModelSerializer):

    short_url = serializers.SerializerMethodField()

    class Meta:
        model = ShortUrl
        fields = ('url', 'short_url',)
        read_only_fields = ('short_url',)

    def get_short_url(self, obj) -> str:
        request = self.context.get('request')
        return f"{request.scheme}://{request.get_host()}{request.get_full_path()}/" + obj.slug

