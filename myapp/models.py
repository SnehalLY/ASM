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


class Department(models.Model):
    dept_name = models.CharField(max_length=100,  unique=True)
    dept_head = models.OneToOneField(DeptHead, on_delete=models.CASCADE, related_name='department_head')
    score = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)  # Store scores up to 999.99

    def __str__(self):
        return f"{self.dept_name}"
    



class Student(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)  # Optional field
    last_name = models.CharField(max_length=100)
    prn = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    event = models.CharField(max_length=50)
    year = models.CharField(max_length=10, choices=[
        ('2nd', 'SY'),
        ('3rd', 'TY'),
        ('4th', 'B.Tech'),
    ])
    department = models.ForeignKey(Department, on_delete=models.CASCADE)  # ForeignKey relationship to Department
    roll_number = models.CharField(max_length=20, unique=True)
    mobile_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.prn})"
    
class winners(models.Model):
    name = models.CharField(max_length=100, unique=True)
    event = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.event}"