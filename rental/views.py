from django.shortcuts import render,redirect
from .forms import CustomerForm,UserForm

# Create your views here.
def homepageView(request):
    context = {}
    return render(request, 'rental/homepage.html', context)

def registerView(request):
    context = {}

    userForm = UserForm(request.POST or None)
    customerForm = CustomerForm(request.POST or None)

    p


    context['userform'] = userForm
    context['customerform'] = customerForm

    return render(request,'rental/register.html',context)

def loginView(request):
    context = {}
    
    
    return render(request,'rental/login.html',context)


def logoutView(request):
    context = {}
    return redirect('login')

    