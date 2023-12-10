from django.urls import path
from project.views import ProjectView, ProjectDetail


urlpatterns = [
    path('projects/', ProjectView.as_view()),
    path('projects/<int:pk>/', ProjectDetail.as_view())
]
