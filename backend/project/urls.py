from django.urls import path
from project.views import ProjectView, ProjectDetail, MessageView, MessageDetail


urlpatterns = [
    path('projects/', ProjectView.as_view()),
    path('projects/<int:pk>/', ProjectDetail.as_view()),
    path('messages/', MessageView.as_view()),
    path('messages/<int:pk>/', MessageDetail.as_view())

]
