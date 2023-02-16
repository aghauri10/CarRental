from django.urls import path
from .views import homepageView,loginView,logoutView,registerView

urlpatterns = [
    path('',homepageView,name = 'homepage'),
    path('login/',loginView,name = 'login'),
    path('register/',registerView,name = 'register'),
    path('logout/',logoutView,name = 'logout'),
    
]
