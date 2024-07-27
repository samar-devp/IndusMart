# authentication/backends.py
from django.contrib.auth.backends import BaseBackend
from .models import User

class PasswordlessAuthBackend(BaseBackend):
    """Log in to Django without providing a password."""

    def authenticate(self, request, email=None):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
