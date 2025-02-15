from django.urls import path
from all_ems.views import *


urlpatterns = [
    path('',home,name='home'),
    path('about/',about, name='about'),
    path('dashboard/',dashboard, name='dashboard'),
    path('all-emp/',all_emp, name='all_emp'),
    path('emp-reg/',emp_reg, name='emp_reg'),
    
    
]



# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')