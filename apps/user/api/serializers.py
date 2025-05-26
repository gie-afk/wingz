from rest_framework import serializers

from apps.user.models import User


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate_email(self, email):
        user = User.objects.filter(email=email)
        if not user.exists():
            error_msg = f"User with email: {email} not found."
            raise serializers.ValidationError(error_msg)

        return email


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "role", "email", "phone_number", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def validate_email(self, email):
        user = User.objects.filter(email=email)
        if user.exists():
            error_msg = f"User with email: {email} already exists. Please user another email."
            raise serializers.ValidationError(error_msg)

        return email

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            role=validated_data["role"],
            phone_number=validated_data["phone_number"],
        )

        user.set_password(password)
        user.save()
        return user
