from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .forms import EmployeeForm, UserForm, EmployeeStockForm, StockForm
from django.contrib.auth.models import User
from .models import Employee, Stock


def employee_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.employee.is_employee_master:
                return HttpResponseRedirect(reverse('employee:employee_details'))
            elif user.employee.is_asset_master:
                return HttpResponseRedirect(reverse('employee:stock_details'))
            else:
                return HttpResponseRedirect(reverse('employee:employee_details'))
        else:
            return render(request, "employee/login.html")
    else:
        if request.user.is_authenticated:
            employee = Employee.objects.all()
            return render(request, "employee/employee_details.html", {"employee": employee})
        return render(request, "employee/login.html")


@login_required(login_url="/")
def add_employee(request):
    if not request.user.employee.is_employee_master:
        return HttpResponseRedirect(reverse('employee:employee_details'))
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        user = UserForm(request.POST)
        if form.is_valid() and user.is_valid():
            first_name = request.POST['first_name']
            username = request.POST['username']
            email = request.POST['email']
            user = User.objects.create_user(first_name, username, email)
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            return HttpResponseRedirect(reverse('employee:employee_details'))
        else:
            return render(request, 'employee/add_employee.html')

    else:
        form = EmployeeForm()
        user = UserForm()
        return render(request, 'employee/add_employee.html', {'form': form, 'user': user})


@login_required(login_url="/")
def employee_details(request):
    employee = Employee.objects.all()
    return render(request, "employee/employee_details.html", {"employee": employee})


@login_required(login_url="/")
def add_stock(request):
    if not request.user.employee.is_asset_master:
        return HttpResponseRedirect(reverse('employee:stock_details'))
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('employee:stock_details'))
    else:
        form = StockForm()
        return render(request,'employee/stock_entry.html', {'form': form})


@login_required(login_url="/")
def stock_details(request):
    stock = Stock.objects.all()
    return render(request, 'employee/stock_details.html', {'stock': stock})


def logout_user(request):
    logout(request)
    return render(request, 'employee/login.html')


@login_required(login_url="/")
def employee_stock_map(request):
    if request.method == "POST":
        form = EmployeeStockForm(request.POST)
        if form.is_valid():
            form.save()
            stock_obj = Stock.objects.get(id=request.POST["asset"])
            stock_obj.no_of_items = stock_obj.no_of_items - 1
            stock_obj.save(update_fields=["no_of_items"])
            return HttpResponseRedirect(reverse('employee:stock_details'), {'form': form})
        else:
            return render(request, "employee/employee_stock.html")
    else:
        form = EmployeeStockForm()
        return render(request, "employee/employee_stock.html",  {'form': form})
