from django.shortcuts import redirect, render
from employee.models import Employee
from employee.forms import EmployeeForm


def update(request,id):
    employee=Employee.objects.get(id=id)
    form=EmployeeForm(request.POST,instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request,'edit.html',{'employee':employee})

def show(request):
    employees=Employee.objects.all()
    return render(request,'show.html',{'employees':employees})


def emp(request):
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/show')


    form=EmployeeForm()
    return render(request,'index.html',{'form':form})

def edit(request,id):
    employee=Employee.objects.get(id=id)
    return render(request,'edit.html',{'employee':employee})