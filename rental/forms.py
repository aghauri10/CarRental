from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Customer


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['gender','dob','occupation','phone_number','license_number']
        widgets = {
            'dob': forms.widgets.DateInput(attrs={'type': 'date'})
        }


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(),required=True)
    
        
        
        