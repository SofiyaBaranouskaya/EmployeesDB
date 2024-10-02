from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm, ProjectForm
from django.shortcuts import render

def add_page(request):
    return render(request, 'employees/add_page.html')

def employee_list(request):
    employees = Employee.objects.all()  # Получаем всех сотрудников

    if request.method == 'POST':
        if 'add' in request.POST:
            form = EmployeeForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('employee_list')
        elif 'delete' in request.POST:
            employee_id = request.POST.get('employee_id')
            employee = get_object_or_404(Employee, id=employee_id)
            employee.delete()
            return redirect('employee_list')
    else:
        form = EmployeeForm()

    return render(request, 'employees/main.html', {'employees': employees, 'form': form})

