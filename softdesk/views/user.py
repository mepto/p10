from django.utils.timezone import now
from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from softdesk.serializers import UserSerializer


class UserViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                  mixins.ListModelMixin, GenericViewSet):
    """View for Users."""
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        """Add creation data to user."""
        serializer = self.get_serializer(data=request.data)
        serializer.initial_data['date_joined'] = now()
        serializer.initial_data['is_staff'] = False
        serializer.initial_data['is_superuser'] = False
        serializer.initial_data['is_active'] = True

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
