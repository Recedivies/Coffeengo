from django.contrib import admin
from django.urls import include, path

from api.views import HealthCheckAPIView, SimpleAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("users.urls")),
    path("", include("rooms.urls")),
    path("test", SimpleAPIView.as_view(), name="test_api_view"),
    path("health", HealthCheckAPIView.as_view(), name="health-check"),
]
