from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from apps.user.models import User
from apps.utils.custom_authentication import AdminUserAuthentication
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [AdminUserAuthentication]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    renderer_classes = [JSONRenderer]
    parser_classes = [JSONParser]
