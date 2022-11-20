from rest_framework import serializers

from softdesk.constants import PROJECT_TYPE
from softdesk.models.project import Project
from softdesk.models.issue import Issue


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


class IssueSerializer(serializers.ModelSerializer):
    """Serialize Issue model."""

    # title = models.CharField()
    # description = models.TextField()
    # assignee_user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    # author_user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    # priority = models.CharField(choices=ISSUE_PRIORITY, max_length=10)
    # status = models.CharField(choices=ISSUE_STATUS, max_length=20)
    # tag = models.CharField(choices=ISSUE_TYPE, max_length=20)
    # project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    # created = models.DateTimeField()
    # created_by = models.ForeignKey(to=User, on_delete=models.CASCADE)
    # modified = models.DateTimeField()
    # modified_by = models.ForeignKey(to=User, on_delete=models.CASCADE)

    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'assignee_user_id', 'author_user_id', 'priority', 'status', 'tag',
                  'project_id', 'created', 'created_by', 'modified', 'modified_by']
