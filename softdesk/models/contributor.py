from django.db import models

from softdesk.constants import CONTRIBUTOR_ROLE
from softdesk.models import Project, User


class Contributor(models.Model):
    """Store contributors."""

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='contributor')
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name='contributor_project')
    role = models.CharField(choices=CONTRIBUTOR_ROLE, max_length=120)
