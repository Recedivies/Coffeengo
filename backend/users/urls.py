from rest_framework import routers

from users.views import AuthViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register("", AuthViewSet, basename="auth")

urlpatterns = router.urls
