from django.utils.timezone import now
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from softdesk.models import Issue
from softdesk.permissions import CanCreateIssueOrComment, IsItemCreatorOrReadOnly
from softdesk.serializers import IssueSerializer


class IssueViewSet(ModelViewSet):
    """View for Issues."""
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = (IsAuthenticated, CanCreateIssueOrComment, IsItemCreatorOrReadOnly,)

    def get_queryset(self):
        """Filter queryset with specific project."""
        queryset = super().get_queryset()
        if 'project_pk' in self.kwargs:
            queryset = queryset.filter(project_id=self.kwargs['project_pk'])
        return queryset

    def perform_create(self, serializer):
        """Add creation date and user to new issue."""
        serializer.validated_data['author_user'] = self.request.user
        serializer.validated_data['created'] = now()
        serializer.validated_data['modified'] = now()
        serializer.validated_data['project_id'] = self.kwargs['project_pk']
        if 'assignee_user' not in serializer.validated_data:
            serializer.validated_data['assignee_user'] = self.request.user
        serializer.save()

    def perform_update(self, serializer):
        """Change modified field on item update."""
        serializer.validated_data['modified'] = now()
        serializer.save()
