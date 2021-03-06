# Generated by Django 3.2.13 on 2022-05-28 14:20

from django.db import migrations


def forwards_func(apps, schema_editor):
    # Get model
    CourseTeachers = apps.get_model("mainapp", "CourseTeachers")
    Courses = apps.get_model("mainapp", "Courses")
    # Create model's objects
    teacher = CourseTeachers.objects.create(
        name_first="Альфред",
        name_second="Нуцубидзе",
        day_birth="1990-07-10",
    )
    teacher.course.set((Courses.objects.get(id="1"), Courses.objects.get(id="3")))

    teacher = CourseTeachers.objects.create(
        name_first="Роман",
        name_second="Доржинов",
        day_birth="1988-02-04",
    )
    teacher.course.set((Courses.objects.get(id="2"), Courses.objects.get(id="4")))

    teacher = CourseTeachers.objects.create(
        name_first="Ярослав",
        name_second="Конягин",
        day_birth="1981-12-08",
    )
    teacher.course.set((Courses.objects.get(id="3"), Courses.objects.get(id="5")))

    teacher = CourseTeachers.objects.create(
        name_first="Автандил",
        name_second="Наварский",
        day_birth="1983-05-16",
    )
    teacher.course.set((Courses.objects.get(id="4"), Courses.objects.get(id="6")))

    teacher = CourseTeachers.objects.create(
        name_first="Роза",
        name_second="Уланова",
        day_birth="1986-05-09",
    )
    teacher.course.set((Courses.objects.get(id="5"), Courses.objects.get(id="7")))

    teacher = CourseTeachers.objects.create(
        name_first="Бронислава",
        name_second="Алиева",
        day_birth="1971-01-07",
    )
    teacher.course.set((Courses.objects.get(id="6"), Courses.objects.get(id="8")))

    teacher = CourseTeachers.objects.create(
        name_first="Диана",
        name_second="Попова",
        day_birth="1990-08-25",
    )
    teacher.course.set((Courses.objects.get(id="1"), Courses.objects.get(id="8")))


def reverse_func(apps, schema_editor):
    # Get model
    CourseTeachers = apps.get_model("mainapp", "CourseTeachers")
    # Delete objects
    CourseTeachers.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0007_lessons_data_migration"),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
