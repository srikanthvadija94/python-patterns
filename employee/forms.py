from django.forms import ModelForm
from .models import Employee, EmployeeStockKeyMap, Stock, User


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        exclude = ['is_employee_master','is_asset_master','user']


class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = "__all__"


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'username','email']


class EmployeeStockForm(ModelForm):
    class Meta:
        model = EmployeeStockKeyMap
        fields = ['employee', 'asset']

    def __init__(self, *args, **kwargs):
        super(EmployeeStockForm, self).__init__(*args, **kwargs)
        self.fields["asset"].queryset = Stock.objects.filter(no_of_items__gt=0)