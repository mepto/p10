from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from softdesk.models import Project
from softdesk.models.contributor import Contributor


class CanCreateIssueOrComment(permissions.BasePermission):
    """Check if user can create comment."""

    def has_permission(self, request, view):
        if request.user in get_object_or_404(Project,
                                             pk=view.kwargs['project_pk']).contributor_users.all():
            return True
        return False


class IsProjectManagerOrReadOnly(permissions.BasePermission):
    """Check that the user is manager in the project."""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Cannot use isinstance due to circular imports
        # pylint: disable=import-outside-toplevel
        from softdesk.views.project import ProjectViewSet

        # pylint: enable=import-outside-toplevel
        if isinstance(view, ProjectViewSet):
            if view.action == 'create':
                return IsAuthenticated
            if view.action in ('update', 'partial_update', 'destroy'):
                if get_object_or_404(Contributor, project_id=view.kwargs['pk'],
                                     user_id=request.user.id).role == 'manager':
                    return True
        if view.action in ('create', 'update', 'partial_update', 'destroy'):
            if get_object_or_404(Contributor, project_id=view.kwargs['project_pk'],
                                 user_id=request.user.id).role == 'manager':
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
