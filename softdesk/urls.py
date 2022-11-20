"""SoftDesk URL Configuration."""
from rest_framework_nested.routers import NestedSimpleRouter

from softdesk.views.comment import CommentViewSet
from softdesk.views.issue import IssueViewSet
from softdesk.views.project import ProjectViewSet

from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')

projects_router = NestedSimpleRouter(router, r'projects', lookup='project')
projects_router.register(r'issues', IssueViewSet, basename='issues')

issues_router = NestedSimpleRouter(projects_router, r'issues', lookup='issue')
issues_router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(projects_router.urls)),
    path('', include(issues_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]


# Point de terminaison d'API	Méthode HTTP	URI
# 1.	Inscription de l'utilisateur	POST	/signup/
# 2.	Connexion de l'utilisateur	POST	/login/

# 8.	Ajouter un utilisateur (collaborateur) à un projet	POST	/projects/{id}/users/
# 9.	Récupérer la liste de tous les utilisateurs (users) attachés à un projet (project)	GET	/projects/{id}/users/
# 10.	Supprimer un utilisateur d'un projet	DELETE	/projects/{id}/users/{id}

# 15.	Créer des commentaires sur un problème	POST	/projects/{id}/issues/{id}/comments/
# 16.	Récupérer la liste de tous les commentaires liés à un problème (issue)	GET	/projects/{id}/issues/{id}/comments/
# 17.	Modifier un commentaire	PUT	/projects/{id}/issues/{id}/comments/{id}
# 18.	Supprimer un commentaire	DELETE	/projects/{id}/issues/{id}/comments/{id}
# 19.	Récupérer un commentaire (comment) via son id	GET	/projects/{id}/issues/{id}/comments/{id}


# DONE
# 3.	Récupérer la liste de tous les projets (projects) rattachés à l'utilisateur (user) connecté	GET	/projects/
# 4.	Créer un projet	POST	/projects/
# 5.	Récupérer les détails d'un projet (project) via son id	GET	/projects/{id}/
# 6.	Mettre à jour un projet	PUT	/projects/{id}/
# 7.	Supprimer un projet et ses problèmes	DELETE	/projects/{id}/

# 11.	Récupérer la liste des problèmes (issues) liés à un projet (project)	GET	/projects/{id}/issues/
# 12.	Créer un problème dans un projet	POST	/projects/{id}/issues/
# 13.	Mettre à jour un problème dans un projet	PUT	/projects/{id}/issues/{id}
# 14.	Supprimer un problème d'un projet	DELETE	/projects/{id}/issues/{id}
