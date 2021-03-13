from django.contrib import admin
from .models import Employee, EmployeeStockKeyMap, Stock

# Register your models here.
admin.site.register(Employee)
admin.site.register(EmployeeStockKeyMap)
admin.site.register(Stock)