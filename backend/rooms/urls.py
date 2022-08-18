from rest_framework import routers

from rooms.views import RoomViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"rooms", RoomViewSet, basename="rooms")

urlpatterns = [
    *router.urls,
]
