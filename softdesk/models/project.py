from django.db import models

from softdesk.constants import PROJECT_TYPE
from softdesk.models import User


class Project(models.Model):
    """Store projects."""
    title = models.CharField(max_length=180)
    description = models.TextField()
    project_type = models.CharField(choices=PROJECT_TYPE, max_length=100)
    author_user = models.ForeignKey(to=User, on_delete=models.CASCADE,
                                    related_name='project_author',
                                    help_text='Author user is not used in permissions')
    contributor_users = models.ManyToManyField(to=User, through='Contributor',
                                               related_name='projects')
