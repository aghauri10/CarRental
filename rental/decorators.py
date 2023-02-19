
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import HttpResponse





def customer_required(view_func):
    '''
    Checks Current User is Customer or not, if not then not allowed to access that page
    '''
    def wrapper(request,*args,**kwargs):
        
        try:
            if request.user.is_authenticated and request.user.customer:
                return view_func(request,*args,**kwargs)
        except:
            pass
        
        if request.user.is_authenticated:# Employee Case
            return HttpResponse("You are not allowed to access this resource. Permission Denied")
        else: # Anonymous 
            return redirect('customer-login')
            
        
        
    wrapper.__doc__ = view_func.__doc__
    wrapper.__name__ = view_func.__name__
    return wrapper
