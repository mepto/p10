"""SoftDesk URL Configuration."""
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from softdesk.views.comment import CommentViewSet
from softdesk.views.contributor import ContributorViewSet
from softdesk.views.issue import IssueViewSet
from softdesk.views.project import ProjectViewSet
from softdesk.views.user import UserViewSet

router = DefaultRouter()
router.register('projects', ProjectViewSet, basename='project')
router.register('signup', UserViewSet, basename='signup')

projects_router = NestedSimpleRouter(router, 'projects', lookup='project')
projects_router.register('issues', IssueViewSet, basename='issues')
projects_router.register('users', ContributorViewSet, basename='users')
issues_router = NestedSimpleRouter(projects_router, 'issues', lookup='issue')
issues_router.register('comments', CommentViewSet, basename='comments')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(projects_router.urls)),
    path('', include(issues_router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token-new'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
