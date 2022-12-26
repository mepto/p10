from rest_framework import status
from rest_framework.response import Response

from softdesk.constants import CONTRIBUTOR_ROLE
from softdesk.models import Project
from softdesk.models.contributor import Contributor
from softdesk.serializers import ProjectSerializer
from softdesk.views.common import SoftDeskView


class ProjectViewSet(SoftDeskView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        Contributor.objects.create(role=CONTRIBUTOR_ROLE[0][0],
                                   project_id=serializer.data['id'],
                                   user_id=serializer.data['author_user'])

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
