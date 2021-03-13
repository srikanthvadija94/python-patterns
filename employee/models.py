from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    phone_no = models.CharField(max_length=13)
    address = models.TextField()
    is_employee_master = models.BooleanField(default=False)
    is_asset_master = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Stock(models.Model):
    name = models.CharField(max_length=150)
    no_of_items = models.IntegerField()
    operating_system = models.CharField(max_length=50)
    specifications = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class EmployeeStockKeyMap(models.Model):
    status_choices = [('Pending', 'Pending'), ('Not Issued', 'Not Issued'), ('With User', 'With User')]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    asset = models.ForeignKey(Stock, on_delete=models.CASCADE)
    issued_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=status_choices, max_length=10)

    def __str__(self):
        return self.employee.user.username
