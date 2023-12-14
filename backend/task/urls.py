from django.urls import path
from task.views import TaskView, TaskDetail

urlpatterns = [
    path('tasks/', TaskView.as_view()),
    path('tasks/<int:pk>/', TaskDetail.as_view())
]
