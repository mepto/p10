from django.utils.timezone import now
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from softdesk.models import Issue
from softdesk.permissions import IsContributor, IsItemCreatorOrReadOnly
from softdesk.serializers import IssueSerializer


class IssueViewSet(ModelViewSet):
    """View for Issues."""
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = (IsAuthenticated, IsContributor, IsItemCreatorOrReadOnly,)

    def list(self, request, *args, **kwargs):
        """List project's issues."""
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
        """Add creation date and user to new issue."""
        serializer = self.get_serializer(data=request.data)
        serializer.initial_data['created'] = now()
        serializer.initial_data['created_by'] = serializer.initial_data['author_user']
        serializer.initial_data['modified'] = now()
        serializer.initial_data['modified_by'] = serializer.initial_data['author_user']
        if 'project' not in serializer.initial_data:
            serializer.initial_data['project'] = self.kwargs['project_pk']
        if 'assignee_user' not in serializer.initial_data:
            serializer.initial_data['assignee_user'] = serializer.initial_data['author_user']

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        """Change modified data to issue on update."""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.initial_data['modified'] = now()
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
