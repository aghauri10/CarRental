
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Employee
from rental.models import Car

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')

        try:
            user = User.objects.get(email = email)
            employee = user.employee
            # If ran successfully till here, then Email user with same mail exists.

            self.add_error('email',f"Employee with same email {email} exists")
        except:
            pass


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['gender','dob','phone_number','company_number']
        widgets = {
            'dob': forms.widgets.DateInput(attrs={'type': 'date'})
        }

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(),required=True)
    

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"