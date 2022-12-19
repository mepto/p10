from django.utils.timezone import now
from rest_framework import status
from rest_framework.response import Response

from softdesk.serializers import UserSerializer
# l'api n'accepte que des access tokens
# quand dépassé, envoyer un invalide
# refresh token requête séparée
from softdesk.views.common import SoftDeskView

# bloquer endpoint;
# class CreateListRetrieveViewSet(mixins.CreateModelMixin,
#                                 mixins.ListModelMixin,
#                                 mixins.RetrieveModelMixin,
#                                 viewsets.GenericViewSet):
#     """
#     A viewset that provides `retrieve`, `create`, and `list` actions.
#
#     To use it, override the class and set the `.queryset` and
#     `.serializer_class` attributes.
#     """
#     pass

# si refresh token toujours valide mais pas access token, alors un nouveau access token est créé


class UserViewSet(SoftDeskView):
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

    # def update(self, request, *args, **kwargs):
    #     """Change modified data to issue on update."""
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.initial_data['modified'] = now()
    #     # TODO update modified by field after authentication
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #
    #     if getattr(instance, '_prefetched_objects_cache', None):
    #         # If 'prefetch_related' has been applied to a queryset, we need to
    #         # forcibly invalidate the prefetch cache on the instance.
    #         instance._prefetched_objects_cache = {}
    #
    #     return Response(serializer.data)
