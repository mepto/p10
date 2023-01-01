from django.utils.timezone import now
from rest_framework import status
from rest_framework.response import Response

from softdesk.models import Comment
from softdesk.serializers import CommentSerializer
from softdesk.views.common import SoftDeskView


class CommentViewSet(SoftDeskView):
    """View for Issues."""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def list(self, request, *args, **kwargs):
        """List project's comments."""
        queryset = self.filter_queryset(self.get_queryset())
        # Add issue pk to filter comments displayed
        if 'issue_pk' in kwargs:
            queryset = queryset.filter(issue_id=kwargs['issue_pk'])
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
        serializer.initial_data['modified'] = now()
        if 'issue' not in serializer.initial_data:
            serializer.initial_data['issue'] = self.kwargs['issue_pk']

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        """Change modified data to comment on update."""
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
