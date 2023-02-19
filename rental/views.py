from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import CustomerForm,UserForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Customer
from.decorators import customer_required

# Create your views here.'
@customer_required
def homepageView(request):
    context = {}
    return render(request, 'rental/homepage.html', context)

def registerView(request):
    context = {}
    
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

    if request.POST:
        messages.error(request,"Check your user data")
    context['userform'] = userForm
    context['customerform'] = customerForm

    return render(request,'rental/register.html',context)

def loginView(request):
    context = {}
    
    if request.user.is_authenticated:
        return redirect('customer-homepage')
    
    form = LoginForm(request.POST or None)

    if form.is_valid():
        data = form.cleaned_data
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request,username = username, password = password)
        
        customer_exists = True
        try:
            customer = user.customer
        except:
            customer_exists = False
        
        if user and customer_exists:
            login(request,user)
            messages.success(request,f'Successfully Logged as {user.username}')
            return redirect('customer-homepage')
        
        messages.error(request,"WRONG USER CREDENTIALS")
        
    
    context['form'] = form
    return render(request,'rental/login.html',context)


def logoutView(request):
    context = {}
    logout(request)
    return redirect('customer-login')

    