from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import CustomerForm,UserForm,LoginForm,UserEditForm,ReviewForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Customer,Car,RentHistory,Reviews
from.decorators import customer_required
from django.http import HttpResponse

@customer_required
def homepageView(request):
    '''
    This is our main Page where customer lands after he/she logged in
    
    Right now,it's empty
    '''
    context = {}
    return render(request, 'rental/homepage.html', context)

@customer_required
def profileEditView(request):
    '''
    User can view his/her profile from here, can also change his details
    '''
    context = {}
    
    # instance is used to fill the form when we already have object with us,else data=request.POST is used
    userform = UserEditForm(instance = request.user)
    customerform = CustomerForm(instance=request.user.customer)
    
    # We will recieve POST data, if user changes his profile data 
    if request.POST or request.FILES:
        
        # Fill form with recieved data
        userform = UserEditForm(request.POST or None,instance=request.user)
        customerform = CustomerForm(request.POST or None,request.FILES or None,instance=request.user.customer)
        
        # If newly recieved data is valid,then change the data and save it
        if userform.is_valid() and customerform.is_valid():
            userform.save()
            customerform.save()
            # userdata = userform.cleaned_data
            # customerdata = customerform.cleaned_data
            
            
            # user.first_name = userdata['first_name']
            # user.last_name = userdata['last_name']
            # user.save()
            
            # customer.gender = customerdata['gender']
            # customer.dob = customerdata['dob']
            # customer.occupation = customerdata['occupation']
            # customer.phone_number = customerdata['phone_number']
            # customer.license_number = customerdata['license_number']
            # customer.profile_pic = customerdata['profile_pic']
            # customer.save()
            
            messages.success(request,"User Profile has been updated")
            return redirect('customer-edit-profile')
            
            
    context['userform'] = userform
    context['customerform'] = customerform

    return render(request, 'rental/profile-edit.html', context)

@customer_required
def profileView(request):
    context = {}
    reviewform = ReviewForm(request.POST or None)

    if reviewform.is_valid():
        reviewform.save()
    
    
    rented_cars = RentHistory.objects.filter(customer = request.user.customer)
    reviews = Reviews.objects.filter(customer = request.user.customer)
    
    # for each car : [reviewform,renthistory,previousreview]
    context['rented_cars'] = rented_cars
    context['reviewform'] = reviewform
    
    return render(request,'rental/profile-view.html', context)
def registerView(request):
    '''
    Register Page for new customer
    '''
    context = {}
    
    # If user is already logged in then user.is_authenticated property sets to True
    if request.user.is_authenticated:
        return redirect('customer-homepage')
    
    
    userForm = UserForm(request.POST or None)
    customerForm = CustomerForm(request.POST or None)
    

    if userForm.is_valid() and customerForm.is_valid():
        user = userForm.save()
        
        customerForm.cleaned_data['user'] = user
        
        customer = Customer.objects.create(**customerForm.cleaned_data)
        
        messages.success(request,f"{user.username} has been successfully created")
        return redirect('customer-login')

    #If POST Data is recieved, and form is not valid, then it means there was some error in form data
    if request.POST:
        messages.error(request,"Check your user data")
    
    context['userform'] = userForm
    context['customerform'] = customerForm

    return render(request,'rental/register.html',context)

def loginView(request):
    '''
    Login Page for registered customers
    '''
    context = {}
    
    # If already logged in, redirect user to homepage
    if request.user.is_authenticated:
        return redirect('customer-homepage')
    
    
    # Creation of Login form, if POST data is recieved then filled with POST else not
    form = LoginForm(request.POST or None)

    if form.is_valid():
        data = form.cleaned_data
        username = data.get('username')
        password = data.get('password')
        
        # authenticate() will return User object if credentials are correct, else None
        user = authenticate(request,username = username, password = password)


        # For customer login, also need to check whether user is customer or not
        if user and hasattr(user,'customer'):
            #login() is used for creation of user sessions
            login(request,user)
            messages.success(request,f'Successfully Logged as {user.username}')
            return redirect('customer-homepage')
        
        messages.error(request,"WRONG USER CREDENTIALS")
        
    
    context['form'] = form
    return render(request,'rental/login.html',context)


def logoutView(request):
    '''
    Clears out User Session details using logout() 
    '''
    context = {}
    logout(request)
    return redirect('customer-login')


@customer_required
def carsListView(request):
    '''
    It lists all the cars available. In future,a user will query 
    For queries, we will change  Car.objects.all() (it fetches all available cars) instead
    we fetch on the basis of query
    '''
    context = {}
    cars = Car.objects.all().order_by('-is_available')
    context['cars'] = cars

    return render(request, 'rental/carsforrent.html', context)

@customer_required
def carRentView(request,car_id):
    context = {}
    
    try:
        car = Car.objects.get(car_id = car_id)
        
        if not car.is_available:
            raise Exception
    except:
        messages.error(request,"Rent Request Cannot Be Completed")
        return redirect('cars-for-rent')
    
    rh_obj = RentHistory.objects.create(customer = request.user.customer,car = car,price = car.price)
    
    # Given car is not available for rent for others
    car.is_available = False
    car.save()
    
    return render(request,'rental/carrent.html',context)