from rest_framework import permissions
from rest_framework.generics import get_object_or_404

from softdesk.models import Project
from softdesk.models.contributor import Contributor


class IsContributor(permissions.BasePermission):
    """Check that the user is a project contributor."""

    def has_permission(self, request, view):
        project = get_object_or_404(Project, pk=view.kwargs['project_pk'])
        if 'project_pk' in view.kwargs and request.user in project.contributor_users.all():
            return True
        return False


class IsProjectManagerOrReadOnly(permissions.BasePermission):
    """Check that the user is manager in the project."""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Find other way to identify view
        if view.action == 'create' and 'ProjectViewSet' in str(view):
            return True
        if view.action in ('create', 'update', 'partial_update', 'destroy') and Contributor.objects.get(
                project_id=view.kwargs['project_pk'], user_id=request.user.id).role == 'manager':
            return True
        return False


class IsItemCreatorOrReadOnly(permissions.BasePermission):
    """
    Check if the request user has created the item.

    For comments and issues. Both have a author_user_id field.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author_user == request.user
