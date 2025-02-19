from django.db import models
import uuid

class Employee(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4 ,editable= False)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    position = models.CharField(max_length=100)  
    department = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)  
    joining_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
