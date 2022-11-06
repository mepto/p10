from django.db import models

from softdesk.models import User


PROJECT_TYPES = (
    ('back_end', 'Back end'),
    ('front_end', 'Front end'),
    ('ios', 'iOS'),
    ('android', 'Android'),
)


class Project(models.Model):
    """Store projects."""
    title = models.CharField(max_length=180)
    description = models.TextField()
    project_type = models.CharField(choices=PROJECT_TYPES, max_length=100)
    author_user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
