from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import ChoiceField

from softdesk.constants import CONTRIBUTOR_ROLE
from softdesk.models import Comment, User
from softdesk.models.contributor import Contributor
from softdesk.models.issue import Issue
from softdesk.models.project import Project


class ProjectSerializer(serializers.ModelSerializer):
    """Serialize Project model."""

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'project_type', 'author_user']


class IssueSerializer(serializers.ModelSerializer):
    """Serialize Issue model."""

    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'assignee_user', 'author_user', 'priority', 'status', 'tag',
                  'project', 'created', 'created_by', 'modified', 'modified_by']


class CommentSerializer(serializers.ModelSerializer):
    """Serialize Comment model."""

    class Meta:
        model = Comment
        fields = ['id', 'description', 'author_user', 'issue', 'created', 'modified']


class ContributorSerializer(serializers.ModelSerializer):
    """Serialize Contributor model."""
    role = ChoiceField(choices=CONTRIBUTOR_ROLE)

    class Meta:
        model = Contributor
        fields = ['id', 'user', 'project', 'role']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError as error:
            raise ValidationError('Cannot comply: duplicate input attempt') from error


class UserSerializer(serializers.ModelSerializer):
    """Serialize User model."""

    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'password1', 'password2', 'username', 'first_name', 'last_name', 'email']

    def create(self, data):

        if data['password1'] == data['password2']:
            data['password'] = data['password1']
            data.pop('password1')
            data.pop('password2')
            user = super().create(data)
            user.set_password(data['password'])
            user.save()
            return user
        raise ValidationError('Passwords do not match. User not created.')
