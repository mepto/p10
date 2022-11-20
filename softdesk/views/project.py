from rest_framework.viewsets import ModelViewSet

from softdesk.models import Project
from softdesk.serializers import ProjectSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
