from django.db import models
from django.db.models import UniqueConstraint

from softdesk.constants import CONTRIBUTOR_ROLE


class Contributor(models.Model):
    """Store contributors."""

    # User string notation instead of object reference to avoid circular import issue
    user = models.ForeignKey(to='softdesk.User', on_delete=models.CASCADE, related_name='contributors')
    project = models.ForeignKey(to='softdesk.Project', on_delete=models.CASCADE, related_name='contributors')
    role = models.CharField(choices=CONTRIBUTOR_ROLE, max_length=120)

    class Meta:
        # Prevent creation if user is already a contributor for this project
        constraints = [UniqueConstraint(fields=['user', 'project'], name='unique_contribution')]
