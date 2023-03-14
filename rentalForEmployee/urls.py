from django.urls import path
from .views import homepageView,loginView,logoutView,registerView,addCarView,profileEditView,profileView,viewAllCustomerView,viewEachCustomerView,viewAllCarsView,viewEachCarView

urlpatterns = [
    path('',homepageView,name = 'employee-homepage'),
    
    # Employee Authentication
    path('login/',loginView,name = 'employee-login'),
    path('register/',registerView,name = 'employee-register'),
    path('logout/',logoutView,name = 'employee-logout'),
    
    # Employee
    path('profile/view/',profileView,name = 'employee-view-profile'),
    path('profile/edit/',profileEditView,name = 'employee-edit-profile'),
    
    
    # Utils
    path('car/',viewAllCarsView,name = 'view-all-cars'),
    path('car/<uuid:id>/',viewEachCarView,name = 'view-car'),
    path('car/add/',addCarView,name = 'add-car'),
    path('customers/',viewAllCustomerView,name='view-customer-all'), # View all customers
    path('customers/<int:id>/',viewEachCustomerView,name='view-customer'),# View Each Customer 
    
    
]
