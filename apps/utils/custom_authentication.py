from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from django.contrib.auth import get_user_model


class AdminUserAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        if not auth_header:
            return None

        try:
            token = self.get_token_from_header(auth_header)
            user = self.validate_token(token)

            if user.role != "admin":
                raise PermissionDenied(f"User: {user.email} has no permission to perform this action.")

            return (user, None)
        except Exception as e:
            raise AuthenticationFailed(str(e))

    def get_token_from_header(self, header):
        try:
            auth_parts = header.split()
            if len(auth_parts) != 2 or auth_parts[0].lower() != "token":
                raise AuthenticationFailed("Invalid token format")

            return auth_parts[1]
        except:
            raise AuthenticationFailed("Invalid token format")

    def validate_token(self, token):
        User = get_user_model()
        try:
            return User.objects.get(auth_token=token)
        except User.DoesNotExist:
            raise AuthenticationFailed("Invalid token")
