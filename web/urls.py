from typing import Any, List

from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns: List[Any] = [
    path("", include("apps.core.urls", namespace="core"), name="core"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += debug_toolbar_urls()
