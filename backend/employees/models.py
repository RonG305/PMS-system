from django.db import models

# Create your models here.


class Employee(models.Model):
    profile = models.ImageField(upload_to='employees/profiles', default='')
    employee_id = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(default='')
    role = models.CharField(max_length=200)
    date_joined = models.DateField()
    date_of_birth = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    county = models.CharField(max_length=200)
    skill_set = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.first_name
