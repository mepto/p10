from django.utils.timezone import now
from rest_framework import mixins, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from softdesk.serializers import UserSerializer


class UserViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                  mixins.ListModelMixin, GenericViewSet):
    """View for Users."""
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        """Add information to user creation."""
        serializer.initial_data['date_joined'] = now()
        serializer.initial_data['is_staff'] = False
        serializer.initial_data['is_superuser'] = False
        serializer.initial_data['is_active'] = True
        serializer.save()
