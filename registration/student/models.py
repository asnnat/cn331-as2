from django.db import models

# Create your models here.
class Student(models.Model):
    username = models.IntegerField()
    password = models.CharField(max_length=64)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{ self.username } ({ self.name })"

class Subject(models.Model):
    subject_id = models.CharField(max_length=5)
    subject_name = models.CharField(max_length=50)
    semester = models.IntegerField()
    year = models.IntegerField()
    max_cap = models.IntegerField()
    status = models.BooleanField()

    def __str__(self):
        return f"{ self.subject_id } { self.subject_name } { self.year }/{ self.semester } ({ self.max_cap }) status: { self.status }"

class Register(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student")
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="subject")

    def __str__(self):
        return f"{ self.student_id } regist { self.subject_id }"