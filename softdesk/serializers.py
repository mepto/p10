from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import ChoiceField, DateTimeField, empty
from rest_framework.relations import PrimaryKeyRelatedField

from softdesk.constants import CONTRIBUTOR_ROLE
from softdesk.models import Comment, User
from softdesk.models.contributor import Contributor
from softdesk.models.issue import Issue
from softdesk.models.project import Project


class ProjectSerializer(serializers.ModelSerializer):
    """Serialize Project model."""

    author_user = PrimaryKeyRelatedField(required=False, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'project_type', 'author_user']


class IssueSerializer(serializers.ModelSerializer):
    """Serialize Issue model."""
    author_user = PrimaryKeyRelatedField(required=False, read_only=True)
    project = PrimaryKeyRelatedField(required=False, read_only=True)
    created = DateTimeField(required=False, read_only=True)
    modified = DateTimeField(required=False, read_only=True)

    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'assignee_user', 'author_user', 'priority', 'status', 'tag',
                  'project', 'created', 'modified']


class CommentSerializer(serializers.ModelSerializer):
    """Serialize Comment model."""
    author_user = PrimaryKeyRelatedField(required=False, read_only=True)
    issue = PrimaryKeyRelatedField(required=False, read_only=True)
    created = DateTimeField(required=False, read_only=True)
    modified = DateTimeField(required=False, read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'description', 'author_user', 'issue', 'created', 'modified']


class ContributorSerializer(serializers.ModelSerializer):
    """Serialize Contributor model."""
    role = ChoiceField(choices=CONTRIBUTOR_ROLE)
    project = PrimaryKeyRelatedField(required=False, read_only=True)

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

    def validate(self, attrs):
        """Return cleaned attrs if passwords match or validation error."""
        attrs = super().validate(attrs)
        if attrs['password1'] == attrs['password2']:
            attrs['password'] = make_password(attrs['password1'])
            attrs.pop('password1')
            attrs.pop('password2')
            return attrs
        raise ValidationError('Passwords do not match. User not created.')
