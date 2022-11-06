"""SoftDesk URL Configuration."""
from rest_framework.urlpatterns import format_suffix_patterns

from softdesk.views.project import ProjectDetailView, ProjectListView

# from django.conf import settings
# from django.db import router
from django.urls import include, path
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'projects', ProjectViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('projects/', ProjectListView.as_view()),
    path('projects/<int:pk>/', ProjectDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
