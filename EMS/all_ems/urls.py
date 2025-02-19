from django.urls import path
from all_ems import views  # Importing views from the correct app

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('employees/', views.all_employees, name='all_employees'),  # Fixed the duplicate name issue
    path('register/', views.emp_reg, name='emp_reg'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('update/<int:emp_id>/', views.update_employee, name='update_employee'),  # Added update route
    path('delete/<int:emp_id>/', views.delete_employee, name='delete_employee'),  # Added delete route
]
