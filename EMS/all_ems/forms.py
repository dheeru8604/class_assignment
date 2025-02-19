from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'phone', 'position', 'department', 'salary']
        # fields = "__all__"
