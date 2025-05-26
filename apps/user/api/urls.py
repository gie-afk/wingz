from django.urls import path, include

from rest_framework import routers

from .views import UserRegistrationView, UserLoginView
from .viewsets import UserViewSet

router = routers.DefaultRouter()
router.register(r"", UserViewSet)


urlpatterns = [
    path("registration/", UserRegistrationView.as_view(), name="user_registration"),
    path("login/", UserLoginView.as_view(), name="user_registration"),
    path("", include(router.urls)),
]
