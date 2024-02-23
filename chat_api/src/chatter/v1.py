from django.urls import path
from rest_framework import routers

from chatter.views import RoomViewSet

router = routers.DefaultRouter()
router.register(r"rooms", RoomViewSet, basename="room")

urlpatterns = []
urlpatterns += router.urls
