from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from softdesk.constants import CONTRIBUTOR_ROLE
from softdesk.models import Project
from softdesk.models.contributor import Contributor
from softdesk.permissions import IsProjectManagerOrReadOnly
from softdesk.serializers import ProjectSerializer


class ProjectViewSet(ModelViewSet):
    """View for projects."""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated, IsProjectManagerOrReadOnly,)

    def create(self, request, *args, **kwargs):
        """Add a new project."""
        self.permission_classes = [IsAuthenticated]
        serializer = self.get_serializer(data=request.data)
        serializer.initial_data['author_user'] = request.user.id
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        Contributor.objects.create(role=CONTRIBUTOR_ROLE[0][0],
                                   project_id=serializer.data['id'],
                                   user_id=request.user.id)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

# TODO: Fix issue with project update and delete on unexisting project
# TODO: Remove author_user from body in issues and comments requests
