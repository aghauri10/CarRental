from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import EmployeeForm,UserForm,LoginForm,CarForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Employee
from .decoraters import employee_required

# Create your views here.

@employee_required
def homepageView(request):
    context = {}

    return render(request,'rentalForEmployee/homepage.html',context)


@employee_required
def addCarView(request):
    context = {}
    
    form = CarForm(request.POST or None,request.FILES or None)
    
    if form.is_valid():
        form.save()
        messages.success(request,"Car Added Successfully")
        return redirect('employee-homepage')
    
    if request.POST and request.FILES:
        messages.error(request,"Enter valid data")
        
    context['form'] = form
    return render(request,'rentalForEmployee/addnewcar.html',context)

def loginView(request):
    context = {}
    
    if request.user.is_authenticated:
        return redirect('employee-homepage')

    form = LoginForm(request.POST or None)

    if form.is_valid():
        data = form.cleaned_data
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request,username = username, password = password)
        
        
        if user and hasattr(user,'employee'):
            login(request,user)
            messages.success(request,f'Successfully Logged as {user.username}')
            return redirect('employee-homepage')
        
        messages.error(request,"WRONG USER CREDENTIALS")
        
    context['form'] = form
    
    
    return render(request,'rentalForEmployee/login.html',context)


def registerView(request):
    context = {}
    
    if request.user.is_authenticated:
        return redirect('employee-homepage')
    
    userform = UserForm(request.POST or None)
    employeeform = EmployeeForm(request.POST or None)
    
    if userform.is_valid() and employeeform.is_valid():
        user = userform.save()
        employeeform.cleaned_data['user'] = user
        employee = Employee.objects.create(**employeeform.cleaned_data)
        
        messages.success(request,f"Employee: {user.username} has been successfully created")
        return redirect('employee-login')
    
    if request.POST:
        messages.error(request,"Check your user data")
        
    context['userform'] = userform
    context['employeeform'] = employeeform
    
    return render(request,'rentalForEmployee/register.html',context)


def logoutView(request):
    context = {}
    logout(request)
    return redirect('employee-login')


