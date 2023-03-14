from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import EmployeeForm,UserForm,LoginForm,CarForm,UserEditForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Employee
from rental.models import Customer,RentHistory,Car
from .decoraters import employee_required
from django.contrib.auth.models import User

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

@employee_required
def viewAllCarsView(request):
    context = {}
    cars = Car.objects.all()
    context['cars'] = cars
    return render(request,'rentalForEmployee/viewallcars.html', context)

@employee_required
def viewEachCarView(request,id):
    context = {}
    try:
        car = Car.objects.get(car_id = id)
    except:
        messages.error(request,"Car doesn't Exists")
        return redirect('view-all-cars')
    
    
    context['car'] = car
    return render(request,'rentalForEmployee/vieweachcar.html', context)

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


@employee_required
def profileEditView(request):
    '''
    User can view his/her profile from here, can also change his details
    '''
    context = {}
    
    # instance is used to fill the form when we already have object with us,else data=request.POST is used
    userform = UserEditForm(instance = request.user)
    employeeform = EmployeeForm(instance=request.user.employee)
    
    # We will recieve POST data, if user changes his profile data 
    if request.POST or request.FILES:
        
        # Fill form with recieved data
        userform = UserEditForm(request.POST or None,instance=request.user)
        employeeform = EmployeeForm(request.POST or None,request.FILES or None,instance=request.user.employee)
        
        # If newly recieved data is valid,then change the data and save it
        if userform.is_valid() and employeeform.is_valid():
            userform.save()
            employeeform.save()
        
            
            messages.success(request,"User Profile has been updated")
            return redirect('employee-edit-profile')
            
            
    context['userform'] = userform
    context['employeeform'] = employeeform

    return render(request, 'rentalForEmployee/profile-edit.html', context)

@employee_required
def profileView(request):
    context = {}
    return render(request,'rentalForEmployee/profile-view.html', context)

@employee_required
def viewAllCustomerView(request):
    context = {}
    customers = Customer.objects.all()
    context['customers'] = customers
    return render(request,'rentalForEmployee/viewallcustomers.html', context)

@employee_required
def viewEachCustomerView(request,id):
    context = {}
    try:
        user = User.objects.get(id = id)
        
        if not hasattr(user,'customer'):
            raise Exception
    except:
        messages.error(request,"Customer doesn't Exists")
        return redirect('view-customer-all')
    
    rented_cars = RentHistory.objects.filter(customer = user.customer)
    
    context['rented_cars'] = rented_cars
    context['user'] = user
    return render(request,'rentalForEmployee/vieweachcustomer.html', context)