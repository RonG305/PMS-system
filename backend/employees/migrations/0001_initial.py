# Generated by Django 4.2.7 on 2023-12-14 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emplyee_id', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=200)),
                ('date_joined', models.DateField()),
                ('date_of_birth', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('county', models.CharField(max_length=200)),
                ('skill_set', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
    ]