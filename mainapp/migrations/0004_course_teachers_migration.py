# Generated by Django 3.2.13 on 2022-05-28 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0003_lessons_migration"),
    ]

    operations = [
        migrations.CreateModel(
            name="CourseTeachers",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name_first", models.CharField(max_length=128, verbose_name="Name")),
                ("name_second", models.CharField(max_length=128, verbose_name="Surname")),
                ("day_birth", models.DateField(verbose_name="Birth date")),
                ("deleted", models.BooleanField(default=False)),
                ("course", models.ManyToManyField(to="mainapp.Courses")),
            ],
        ),
    ]
