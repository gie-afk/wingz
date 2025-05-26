from django.urls import path, include

from rest_framework import routers

from .viewsets import RideViewSet

router = routers.DefaultRouter()
router.register(r"", RideViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
