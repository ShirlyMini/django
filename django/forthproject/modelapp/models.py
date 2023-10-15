from django.db import models

# Create your models here.

class Student(models.Model):
    stud_name=models.CharField(max_length=20)
    stud_dept=models.CharField(max_length=10)
    stud_marks=models.IntegerField()

    def __str__(self):
        return f'student {self.stud_name} added sucessfully'