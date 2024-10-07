# admin.py

from django.contrib import admin
from .models import DeptHead, Student, Department, winners
from .forms import DeptHeadForm

@admin.register(DeptHead)
class DeptHeadAdmin(admin.ModelAdmin):
    form = DeptHeadForm
    list_display = ('username',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'prn', 'email', 'department', 'year', 'roll_number' , 'event')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dept_name' , 'dept_head' , 'score')

@admin.register(winners)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name' , 'event')
