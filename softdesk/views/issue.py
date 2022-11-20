from django.utils.timezone import now
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from softdesk.models import Issue
from softdesk.serializers import IssueSerializer


class IssueViewSet(ModelViewSet):
    """View for Issues."""
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    def create(self, request, *args, **kwargs):
        """Add creation date and user to new issue."""
        serializer = self.get_serializer(data=request.data)
        serializer.initial_data['created'] = now()
        serializer.initial_data['created_by'] = serializer.initial_data['author_user_id']
        serializer.initial_data['modified'] = now()
        serializer.initial_data['modified_by'] = serializer.initial_data['author_user_id']
        if 'project_id' not in serializer.initial_data:
            serializer.initial_data['project_id'] = self.kwargs['project_pk']
        if 'assignee_user_id' not in serializer.initial_data:
            serializer.initial_data['assignee_user_id'] = serializer.initial_data['author_user_id']

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
