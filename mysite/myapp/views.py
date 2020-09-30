from django.shortcuts import render
from .models import employee
from .resources import EmployeeResources
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse

def simple_upload(request):
    if request.method == 'POST':
        employee_resource = EmployeeResources()
        dataset = Dataset()
        new_employee = request.FILES['myfile']

        if not new_employee.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request,'upload.html')

        imported_data = dataset.load(new_employee.read(),format='xlsx')
        for data in imported_data:
            value = employee(
                 data[0],
                 data[1],
                 data[2],
                 data[3]
                 )
            value.save()
    return render(request,'upload.html')




