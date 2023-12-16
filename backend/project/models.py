from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=20)
    description = models.TextField()
    priority_level = models.CharField(max_length=200)
    date_posted = models.DateField()
    deadline = models.DateField()

    def __str__(self):
        return self.name


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    projectId = models.ForeignKey(Project, on_delete=models.CASCADE)

    def formated_date_time(self):
        return self.timestamp.strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f'{self.sender } sent message'
