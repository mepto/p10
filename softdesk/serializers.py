from rest_framework import serializers

from softdesk.models import Comment
from softdesk.models.issue import Issue
from softdesk.models.project import Project


class ProjectSerializer(serializers.ModelSerializer):
    """Serialize Project model."""

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'project_type', 'author_user_id']


class IssueSerializer(serializers.ModelSerializer):
    """Serialize Issue model."""

    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'assignee_user_id', 'author_user_id', 'priority', 'status', 'tag',
                  'project_id', 'created', 'created_by', 'modified', 'modified_by']


class CommentSerializer(serializers.ModelSerializer):
    """Serialize Comment model."""

    class Meta:
        model = Comment
        fields = ['id', 'description', 'author_user_id', 'issue_id', 'created', 'modified']
