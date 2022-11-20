from django.db import models

from softdesk.constants import ISSUE_PRIORITY, ISSUE_STATUS, ISSUE_TYPE
from softdesk.models import User
from softdesk.models.project import Project


class Issue(models.Model):
    """Store issues."""
    # assignee defaults to user creator
    title = models.CharField(max_length=180)
    description = models.TextField()
    assignee_user_id = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='issue_assignee')
    author_user_id = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='issue_author')
    priority = models.CharField(choices=ISSUE_PRIORITY, max_length=10)
    status = models.CharField(choices=ISSUE_STATUS, max_length=20)
    tag = models.CharField(choices=ISSUE_TYPE, max_length=20)
    project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name='issue_project')
    created = models.DateTimeField()
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='issue_creator')
    modified = models.DateTimeField()
    modified_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='issue_modifier')


