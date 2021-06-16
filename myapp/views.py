from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request,'myapp/home.html')

def about(request):
    return HttpResponse('we are students')

def form(request):
    return render(request,'myapp/form.html')

def form1(request):
    return render(request,'myapp/form1.html')


def countries(request):
    return render(request,'myapp/countries.html',{'countries':['france','Italy','Spain']})

def number(request):
    list1=list('123456789abcd')
    thenumber=''
    length=10
    for x in range(length):
        thenumber=thenumber+random.choice(list1)
    return render(request,'myapp/number.html',{'number':thenumber})