from django.shortcuts import redirect
from django.http import HttpResponse


# login_required decorater(in built one) is not enough,as customer/employee is attached to user, login_required only checks for user authentication. Customer required checks both user authentication as well as checks whether customer instance is associated with user or not
def customer_required(view_func):
    '''
    Checks Current User is Customer or not, if not then not allowed to access that page
    '''
    def wrapper(request,*args,**kwargs):
        
        if request.user.is_authenticated and hasattr(request.user,'customer'):#Customer User
            return view_func(request,*args,**kwargs)
        
        elif request.user.is_authenticated and hasattr(request.user,'employee'):# Employee User
            return HttpResponse("You are not allowed to access this resource. Permission Denied")
        
        # Anonymous User 
        return redirect('customer-login')
            
        
    # These are optional lines, as decorating a function changes a function attributes like name and docstring for function,so we manually assign it to our new function wrapper that will replace our function after decoration
    wrapper.__doc__ = view_func.__doc__
    wrapper.__name__ = view_func.__name__
    return wrapper
