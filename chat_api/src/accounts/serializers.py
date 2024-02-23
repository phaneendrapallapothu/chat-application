from django.contrib.auth import authenticate
from django.db import IntegrityError
from rest_framework import serializers
from accounts.models import User, Token


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "date_joined",
            "last_login",
            "password",
            "confirm_password",
        ]

    def validate(self, attrs):
        confirm_password = attrs.pop("confirm_password")
        if attrs["password"] != confirm_password:
            raise serializers.ValidationError(
                "Password and Confirm Password must match"
            )
        return attrs

    def create(self, validated_data):
        try:
            return self.Meta.model.objects.create_user(**validated_data)
        except IntegrityError:
            raise serializers.ValidationError("Username already exists")


class TokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True, source="key")

    class Meta:
        model = Token
        fields = ["username", "password", "token"]

    def validate(self, attrs):
        username = attrs.pop("username")
        password = attrs.pop("password")
        if username and password:
            user = authenticate(
                request=self.context.get("request"),
                username=username,
                password=password,
            )
            if not user:
                raise serializers.ValidationError("Invalid username or password")
        else:
            raise serializers.ValidationError("Username and password are required")
        attrs["user"] = user
        return attrs

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            return self.Meta.model.objects.get(user=validated_data["user"])
