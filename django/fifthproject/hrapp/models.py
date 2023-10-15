from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_no = models.IntegerField()
    emp_name = models.CharField(max_length=20)
    emp_sal = models.FloatField()
    emp_addr = models.CharField(max_length=200)

    def __str__(self):
        return f'Employee {self.emp_name} added successfully'