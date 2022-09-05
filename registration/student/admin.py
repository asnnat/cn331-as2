from django.contrib import admin

from .models import Student, Subject, Register

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ("username", "password", "name")

class SubjectAdmin(admin.ModelAdmin):
    list_display = ("subject_id", "subject_name", "semester", "year", "max_cap", "status")

admin.site.register(Student, StudentAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Register)