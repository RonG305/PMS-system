# Generated by Django 4.2.7 on 2023-12-15 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_employee_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]