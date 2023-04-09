from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from softdesk.models import Comment
from softdesk.permissions import CanCreateIssueOrComment, IsItemCreatorOrReadOnly
from softdesk.serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    """View for Issues."""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, CanCreateIssueOrComment, IsItemCreatorOrReadOnly)

    def get_queryset(self):
        """Filter queryset with specific project."""
        queryset = super().get_queryset()
        if 'issue_pk' in self.kwargs:
            queryset = queryset.filter(issue_id=self.kwargs['issue_pk'])
        return queryset

    def perform_create(self, serializer):
        """Add creation date and user to new issue."""
        serializer.save(
            author_user=self.request.user,
            issue_id=self.kwargs['issue_pk']
        )
