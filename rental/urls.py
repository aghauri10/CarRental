from django.urls import path
from .views import homepageView,loginView,logoutView,registerView,carsListView,profileView,profileEditView,carRentView

urlpatterns = [
    # Customer Authentication
    path('',homepageView,name = 'customer-homepage'),
    path('login/',loginView,name = 'customer-login'),
    path('register/',registerView,name = 'customer-register'),
    path('logout/',logoutView,name = 'customer-logout'),
    
    # Customer Details
    path('profile/view/',profileView,name = 'customer-view-profile'),
    path('profile/edit/',profileEditView,name = 'customer-edit-profile'),
    
    # Car
    path('cars/',carsListView,name='cars-for-rent'),
    path('car/rent/<uuid:car_id>/',carRentView,name='rent-car'),
    
]
