from django.urls import path
from rest_framework import routers

from accounts.views import (
    RegisterAPIView,
    LoginAPIView,
    LogoutAPIView,
    UserListAPIView,
    DetailAPIView,
)

router = routers.DefaultRouter()

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("logout/", LogoutAPIView.as_view(), name="logout"),
    path("detail/", DetailAPIView.as_view(), name="detail"),
    path("users/", UserListAPIView.as_view(), name="users"),
]
urlpatterns += router.urls
