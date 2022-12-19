from django.db import models

from softdesk.models import User
from softdesk.models.issue import Issue


class Comment(models.Model):
    """Store comments."""

    description = models.TextField()
    author_user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    issue = models.ForeignKey(to=Issue, on_delete=models.CASCADE)
    created = models.DateTimeField()
    modified = models.DateTimeField()
