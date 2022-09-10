from django.contrib import admin

from .models import Subject, Student, Register

class StudentAdmin(admin.ModelAdmin):
    list_display = ['username', 'first', 'last']
    
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'name', 'semester', 'year', 'max_cap', 'status']

admin.site.register(Student, StudentAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Register)