from rest_framework import serializers

from softdesk.models.project import Project


class ProjectSerializer(serializers.ModelSerializer):
    """Serialize Project model."""

    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(required=True, allow_blank=False, max_length=120)
    # description = serializers.CharField(style={'base_template': 'textarea.html'})
    # project_type = serializers.ChoiceField(choices=PROJECT_TYPES, required=True)
    # author_user_id = serializers.IntegerField()

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'project_type', 'author_user_id']

