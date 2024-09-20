# models.py
from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class DeptHead(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)  # Store hashed passwords

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)  # Optional field
    last_name = models.CharField(max_length=100)
    prn = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    year = models.CharField(max_length=10, choices=[
        ('2nd', 'SY'),
        ('3rd', 'TY'),
        ('4th', 'B.Tech'),
    ])
    department = models.CharField(max_length=50, choices=[
        ('Computer', 'Computer'),
        ('IT', 'IT'),
        ('Mechanical', 'Mechanical'),
    ])
    roll_number = models.CharField(max_length=20, unique=True)
    mobile_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.prn})"