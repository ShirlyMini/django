from django.shortcuts import render, redirect
from hrapp.models import Employee
from hrapp.forms import EmployeeReg

# Create your views here.

def employee_info(request):
    emp_data=Employee.objects.all()
    return render(request, 'hrapp/index.html', {'employee_data':emp_data})

def employee_req(request):
    form = EmployeeReg()
    if request.method == 'POST':
        form = EmployeeReg(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/data')
    return render(request, 'hrapp/reg.html', {'from': form})

def employee_delete(request, id):
    emp_data = Employee.objects.get(id=id)
    emp_data.delete()
    return redirect('/data')

def employee_update(request, id):
    emp_data = Employee.objects.get(id=id)
    if request.method == 'POST':
        form = EmployeeReg(request.POST, instance=emp_data) #####
        if form.is_valid():
            form.save()
            return redirect('/data')
    return render(request, 'hrapp/update.html', {'data': emp_data})