from django.contrib.auth import authenticate

from rest_framework import generics, permissions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


from .serializers import UserSerializer, UserLoginSerializer


class UserRegistrationView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserLoginView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(**serializer.data)

        if user is None:
            return Response({"code": 400, "errors": {"detail": "Invalid password supplied", "source": "password"}})

        token, created = Token.objects.get_or_create(user=user)

        return Response({"token": token.key})
