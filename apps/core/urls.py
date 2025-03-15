from typing import List

from django.urls import URLPattern, path

from . import views

app_name: str = "core"

urlpatterns: List[URLPattern] = [
    path("", views.IndexView.as_view(), name="index"),
    path("policy/", views.PolicyView.as_view(), name="policy"),
]
