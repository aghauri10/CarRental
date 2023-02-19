from django.urls import path
from .views import homepageView,loginView,logoutView,registerView,carsListView

urlpatterns = [
    path('',homepageView,name = 'customer-homepage'),
    path('login/',loginView,name = 'customer-login'),
    path('register/',registerView,name = 'customer-register'),
    path('logout/',logoutView,name = 'customer-logout'),
    
    path('cars/',carsListView,name='cars-for-rent'),
    
]
