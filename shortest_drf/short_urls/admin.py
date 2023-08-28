from django.contrib import admin

from shortest_drf.short_urls.models import ShortUrl


class ShortUrlAdmin(admin.ModelAdmin):
    ordering = ('-created_at',)


admin.site.register(ShortUrl, ShortUrlAdmin)
