from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

__all__ = ["User", "Token"]
