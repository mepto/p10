from django.utils.timezone import now
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from softdesk.models import Comment
from softdesk.serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    """View for Issues."""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

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
