# Generated by Django 4.1.1 on 2022-10-05 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regist', '0004_rename_student_id_register_student_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='student',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='student', to='regist.student'),
        ),
        migrations.AlterField(
            model_name='register',
            name='subject',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='regist.subject'),
        ),
    ]