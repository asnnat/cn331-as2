# Generated by Django 4.1 on 2022-09-05 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Subject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subject_id", models.IntegerField()),
                ("subject_name", models.CharField(max_length=50)),
                ("semester", models.IntegerField()),
                ("year", models.IntegerField()),
                ("max_cap", models.IntegerField()),
                ("status", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="Register",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "student_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="student",
                        to="student.student",
                    ),
                ),
                (
                    "subject_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subject",
                        to="student.subject",
                    ),
                ),
            ],
        ),
    ]