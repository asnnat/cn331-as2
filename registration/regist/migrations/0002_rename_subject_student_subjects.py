# Generated by Django 4.1.1 on 2022-09-10 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("regist", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="student",
            old_name="subject",
            new_name="subjects",
        ),
    ]
