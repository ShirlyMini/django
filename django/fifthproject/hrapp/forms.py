from django import forms
from hrapp.models import Employee
# Create your models here.

class EmployeeReg(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        # exclude = ['empno']

