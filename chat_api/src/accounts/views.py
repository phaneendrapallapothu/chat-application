from django.db.models import Q
from rest_framework import generics, permissions

from accounts.models import User, Token
from accounts.serializers import UserSerializer, TokenSerializer


class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class LoginAPIView(generics.CreateAPIView):
    serializer_class = TokenSerializer
    permission_classes = [permissions.AllowAny]


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.filter(~Q(username="AnonymousUser"), is_active=True)
    serializer_class = UserSerializer


class DetailAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class LogoutAPIView(generics.DestroyAPIView):
    queryset = Token.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        return queryset.get(user=self.request.user)
