from django.db import models
from employees.models import Employee

# Create your models here.


class Task(models.Model):

    task_name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=200, default='incomplete')
    team_leader = models.CharField(max_length=200)
    assignned_mebers = models.ManyToManyField(Employee)
    description = models.TextField()

    def __str__(self):
        return self.task_name
