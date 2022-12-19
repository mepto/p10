from softdesk.models import Project
from softdesk.serializers import ProjectSerializer
from softdesk.views.common import SoftDeskView


class ProjectViewSet(SoftDeskView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
