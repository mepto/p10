from rest_framework import status
from rest_framework.response import Response

from softdesk.models.contributor import Contributor
from softdesk.serializers import ContributorSerializer
from softdesk.views.common import SoftDeskView


class ContributorViewSet(SoftDeskView):
    """View for contributor."""
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer

    def list(self, request, *args, **kwargs):
        """List project's contributors."""
        queryset = self.filter_queryset(self.get_queryset())
        # Add project pk to filter issues displayed
        if 'project_pk' in kwargs:
            queryset = queryset.filter(project_id=kwargs['project_pk'])
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """Add contributor to project."""
        serializer = self.get_serializer(data=request.data)
        if 'project' not in serializer.initial_data:
            serializer.initial_data['project'] = self.kwargs['project_pk']
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
