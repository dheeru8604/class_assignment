from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Employee  
from .forms import EmployeeForm

# Home Page
def home(request):
    return render(request, 'home.html')

# Dashboard
def dashboard(request):
    total_employees = Employee.objects.count()  
    return render(request, 'dashboard.html', {'total_emp': total_employees})

# View All Employees
def all_employees(request):
    employees = Employee.objects.all()  
    return render(request, 'all_emp.html', {'employees': employees})

# Employee Registration
def emp_reg(request):  
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee registered successfully!")
            return redirect('all_employees')  
        else:
            messages.error(request, "Error in form submission")
    else:
        form = EmployeeForm()
    
    return render(request, 'emp_reg.html', {'form': form})

# Update Employee
def update_employee(request, emp_id):
    employee = get_object_or_404(Employee, id=emp_id)
    
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee updated successfully!")
            return redirect('all_employees')
        else:
            messages.error(request, "Error in updating employee")
    else:
        form = EmployeeForm(instance=employee)
    
    return render(request, 'update_emp.html', {'form': form, 'employee': employee})

# Delete Employee
def delete_employee(request, emp_id):
    employee = get_object_or_404(Employee, id=emp_id)
    employee.delete()
    messages.success(request, "Employee deleted successfully!")
    return redirect('all_employees')

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")
    
    return render(request, 'login.html')

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')
