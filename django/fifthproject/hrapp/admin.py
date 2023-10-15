from django.contrib import admin
from hrapp.models import Employee

# Register your models here.
class EmployeeData(admin.ModelAdmin):
    list=["emp_no", "emp_name", "emp_sal", "emp_addr"]

admin.site.register(Employee, EmployeeData)
