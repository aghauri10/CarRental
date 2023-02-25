
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import HttpResponse

def employee_required(view_func):
    def wrapper(request,*args,**kwargs):
        
        if request.user.is_authenticated and hasattr(request.user,'employee'):# Employee User
            return view_func(request,*args,**kwargs)
        
        elif request.user.is_authenticated and hasattr(request.user,'customer'):#Customer User
            return HttpResponse("You are not allowed to access this resource. Permission Denied")
        
        # Anonymous User 
        return redirect('employee-login')
        
    wrapper.__doc__ = view_func.__doc__
    wrapper.__name__ = view_func.__name__
    return wrapper
