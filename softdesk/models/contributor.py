# from django.db import models
#
# from softdesk.models import Project, User
#
#
# class Contributor(models.Model):
#     """Store contributors."""
#
#     user_id = models.ForeignKey(to=User)
#     project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE())
#     permission = models.CharField()
#     role = models.CharField()
