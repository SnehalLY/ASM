# admin.py

from django.contrib import admin
from .models import DeptHead, Student
from .forms import DeptHeadForm

@admin.register(DeptHead)
class DeptHeadAdmin(admin.ModelAdmin):
    form = DeptHeadForm
    list_display = ('username',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'prn', 'email', 'department', 'year', 'roll_number')
