from django.urls import path
from .views import homepageView,loginView,logoutView,registerView,addCarView

urlpatterns = [
    path('',homepageView,name = 'employee-homepage'),
    
    # Employee Authentication
    path('login/',loginView,name = 'employee-login'),
    path('register/',registerView,name = 'employee-register'),
    path('logout/',logoutView,name = 'employee-logout'),
    
    # Utils
    path('car/add/',addCarView,name = 'add-car'),
    
    
    
]
