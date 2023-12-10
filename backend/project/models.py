from django.db import models

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
