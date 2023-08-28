from django.urls import path
from rest_framework.routers import DefaultRouter

from shortest_drf.api.views.short_urls.create import ShortUrlCreateView
from shortest_drf.api.views.short_urls.retrieve import ShortUrlRetrieveView

router = DefaultRouter()

urlpatterns = router.urls + [
    path('short_urls', ShortUrlCreateView.as_view(), name="short_url_create_view"),
    path('short_urls/<slug:slug>', ShortUrlRetrieveView.as_view(), name="short_url_retrieve_view"),
]
