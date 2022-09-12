from django.db import models

class Student(models.Model):
    username = models.CharField(max_length=50)
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)

    def __str__(self):
        return f'{ self.username }'
        
class Subject(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    semester = models.IntegerField()
    year = models.IntegerField()
    max_cap = models.IntegerField()
    status = models.BooleanField()

    def __str__(self):
        return f"{ self.code } { self.name }"

class Register(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="subject")

    def __str__(self):
        return f"{ self.student } { self.subject }"