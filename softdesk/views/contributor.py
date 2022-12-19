from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from softdesk.models.contributor import Contributor
from softdesk.serializers import ContributorSerializer


class ContributorViewSet(ModelViewSet):
    """View for contributor."""
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer

    def create(self, request, *args, **kwargs):
        """Add contributor to project."""
        serializer = self.get_serializer(data=request.data)
        if 'project' not in serializer.initial_data:
            serializer.initial_data['project'] = self.kwargs['project_pk']
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
