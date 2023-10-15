from django.contrib import admin
from modelapp.models import Student

# Register your models here.
class Studentinfo(admin.ModelAdmin):
    student_info=["stud_name", "stud_dept", "stud_marks"]


admin.site.register(Student, Studentinfo)
