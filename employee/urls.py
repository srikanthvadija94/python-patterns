from django.urls import path
from . import views

app_name = "employee"
urlpatterns = [
    path("", views.employee_login, name='employee_login'),
    path("employee_details/", views.employee_details, name='employee_details'),
    path("add_employee/", views.add_employee, name='add_employee'),
    path("add_stock/", views.add_stock, name='add_stock'),
    path("stock_details/", views.stock_details, name='stock_details'),
    path("logout_user/", views.logout_user, name='logout_user'),
    path("employee_stock_map/", views.employee_stock_map, name='employee_stock_map'),
    ]