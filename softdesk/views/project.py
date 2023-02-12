from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from softdesk.constants import CONTRIBUTOR_ROLE, MANAGER
from softdesk.models import Project
from softdesk.models.contributor import Contributor
from softdesk.permissions import IsProjectManagerOrReadOnly
from softdesk.serializers import ProjectSerializer


class ProjectViewSet(ModelViewSet):
    """View for projects."""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated, IsProjectManagerOrReadOnly)

    def __str__(self):
        return 'ProjectViewSet'

    def perform_create(self, serializer):
        """Populate author_user information before save."""
        serializer.validated_data['author_user'] = self.request.user
        project = serializer.save()
        Contributor.objects.create(role=MANAGER,
                                   project_id=project.id,
                                   user_id=int(self.request.user.id))
