# from django.db import models
#
# from softdesk.models import User
# from softdesk.models.project import Project
#
#
# class Issue(models.Model):
#     """Store issues."""
#     # assignee defaults to user creator
#     # Priority levels LOW MEDIUM HIGH
#     # Statuses  To do, In progress, Done, Cancelled
#     # tags Bug, Improvement, Task
#     title = models.CharField()
#     description = models.TextField()
#     assignee_user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
#     author_user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
#     priority = models.CharField()
#     status = models.CharField()
#     tag = models.CharField()
#     project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE)
#     created = models.DateTimeField()
#     created_by = models.ForeignKey(to=User, on_delete=models.CASCADE)
#     modified = models.DateTimeField()
#     modified_by = models.ForeignKey(to=User, on_delete=models.CASCADE)
#
#
