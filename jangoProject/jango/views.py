from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html', {'name' : 'kunal'})

def add(request):
    value1 = int(request.POST['num1'])
    value2 = int(request.POST['num2'])
    result = value1 + value2
    return render(request, 'result.html', {'result' :  result})