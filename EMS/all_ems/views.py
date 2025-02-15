from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
  return render(request,'home.html')

def about(request):
  return render(request,'about.html')

def dashboard(request):
  return render(request,'dashboard.html')

def all_emp(request):
  return render(request,'all_emp.html')


def emp_reg(request):
  return render(request,'emp_reg.html')
  


