from django.utils.timezone import now
from rest_framework import mixins
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from softdesk.serializers import UserSerializer


class UserViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                  mixins.ListModelMixin, GenericViewSet):
    """View for Users."""
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        """Add information to user creation."""
        serializer.save(
            date_joined=now(),
            is_staff=False,
            is_superuser=False,
            is_active=True
        )
