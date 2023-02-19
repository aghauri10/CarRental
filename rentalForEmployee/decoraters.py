
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import HttpResponse

def employee_required(view_func):
    def wrapper(request,*args,**kwargs):
        
        try:
            if request.user.is_authenticated and request.user.employee:
                return view_func(request,*args,**kwargs)
        except Exception as e:
            pass
        
        if request.user.is_authenticated:# Customer Case
            return HttpResponse("You are not allowed to access this resource. Permission Denied")
        else: # Anonymous 
            return redirect('employee-login')
        
    wrapper.__doc__ = view_func.__doc__
    wrapper.__name__ = view_func.__name__
    return wrapper
