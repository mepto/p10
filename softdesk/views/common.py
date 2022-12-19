from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class SoftDeskView(ModelViewSet):
    """Set base view for softdesk classes."""
    permission_classes = (IsAuthenticated,)
