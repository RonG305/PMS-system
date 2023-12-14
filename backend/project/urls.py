from django.urls import path
from project.views import ProjectView, ProjectDetail, GitubProjects, GitubView


urlpatterns = [
    path('projects/', ProjectView.as_view()),
    path('projects/<int:pk>/', ProjectDetail.as_view()),
    path('gitub/', GitubProjects.as_view()),
    path('gitub/<int:pk>/', GitubView.as_view())
]
