# Generated by Django 4.2.7 on 2023-12-15 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_employee_email'),
        ('task', '0003_rename_decription_task_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='assignned_mebers',
            field=models.ManyToManyField(to='employees.employee'),
        ),
    ]