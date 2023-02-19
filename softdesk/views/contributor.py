from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from softdesk.models.contributor import Contributor
from softdesk.permissions import IsProjectManagerOrReadOnly
from softdesk.serializers import ContributorSerializer


class ContributorViewSet(ModelViewSet):
    """View for contributor."""
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = (IsAuthenticated, IsProjectManagerOrReadOnly)
    lookup_field = 'user_id'

    def get_queryset(self):
        """Filter queryset with specific project."""
        queryset = super().get_queryset()
        if 'project_pk' in self.kwargs:
            queryset = queryset.filter(project_id=self.kwargs['project_pk'])
        if 'pk' in self.kwargs:
            queryset = queryset.filter(user_id=self.kwargs['pk'])
        return queryset

    def perform_create(self, serializer):
        """Add project id to serializer data."""
        serializer.validated_data['project_id'] = self.kwargs['project_pk']
        serializer.save()
