from django.shortcuts import render
from modelapp.models import Student
from modelapp.forms import Studentregister
# Create your views here.

def student_det(request):
    data = Student.objects.all()
    reg = Studentregister()
    dict1={"stud_info":data, "stud_reg": reg}
    return render(request, 'modelapp/index.html', context=dict1)

