from django.urls import path
from employees.views import EmployeeView, EmployeeDetail

urlpatterns = [
    path('employees/', EmployeeView.as_view()),
    path('employees/<int:pk>/', EmployeeDetail.as_view())
]
