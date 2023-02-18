from django.urls import path
from .views import homepageView,loginView,logoutView,registerView

urlpatterns = [
    path('',homepageView,name = 'customer-homepage'),
    path('login/',loginView,name = 'customer-login'),
    path('register/',registerView,name = 'customer-register'),
    path('logout/',logoutView,name = 'customer-logout'),
    
]
