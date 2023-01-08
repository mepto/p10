from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from softdesk.models.contributor import Contributor
from softdesk.permissions import IsContributor, IsProjectManagerOrReadOnly
from softdesk.serializers import ContributorSerializer


class ContributorViewSet(ModelViewSet):
    """View for contributor."""
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = (IsAuthenticated, IsContributor, IsProjectManagerOrReadOnly)

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

    def retrieve(self, request, *args, **kwargs):
        """Retrieve data for a project contributor."""
        instance = self.queryset.get(project_id=kwargs['project_pk'], user_id=kwargs['pk'])
        serializer = self.get_serializer(instance)
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

    def update(self, request, *args, **kwargs):
        """Change modified data to project contributor on update."""
        partial = kwargs.pop('partial', False)
        instance = self.queryset.get(project_id=kwargs['project_pk'], user_id=kwargs['pk'])
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """Delete a project contributor."""
        instance = self.queryset.get(project_id=kwargs['project_pk'], user_id=kwargs['pk'])
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
