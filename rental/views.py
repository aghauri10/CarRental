from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import CustomerForm,UserForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Customer

# Create your views here.'
@login_required(login_url='login/')
def homepageView(request):
    context = {}
    return render(request, 'rental/homepage.html', context)

def registerView(request):
    context = {}
    
    if request.user.is_authenticated:
        return redirect('homepage')
    
    userForm = UserForm(request.POST or None)
    customerForm = CustomerForm(request.POST or None)
    

    if userForm.is_valid() and customerForm.is_valid():
        user = userForm.save()
        
        customerForm.cleaned_data['user'] = user
        
        customer = Customer.objects.create(**customerForm.cleaned_data)
        
        messages.success(request,f"{user.username} has been successfully created")
        return redirect('login')

    messages.error(request,"Check your user data")
    context['userform'] = userForm
    context['customerform'] = customerForm

    return render(request,'rental/register.html',context)

def loginView(request):
    context = {}
    
    if request.user.is_authenticated:
        return redirect('homepage')
    
    form = LoginForm(request.POST or None)

    if form.is_valid():
        data = form.cleaned_data
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request,username = username, password = password)
        
        if user:
            login(request,user)
            messages.success(request,f'Successfully Logged as {user.username}')
            return redirect('homepage')
        
        messages.error(request,"WRONG USER CREDENTIALS")
        
    
    context['form'] = form
    return render(request,'rental/login.html',context)


def logoutView(request):
    context = {}
    logout(request)
    return redirect('login')

    