from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Customer


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')

        try:
            user = User.objects.get(email = email)
            customer = user.customer
            # If ran successfully till here, then customer user with same mail exists.

            self.add_error('email',f"Customer with same email {email} exists")
        except User.MultipleObjectsReturned:
            self.add_error('email',f"Customer with same email {email} exists")
        except:
            pass
            
        
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']
    
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['gender','dob','occupation','phone_number','license_number','profile_pic']
        widgets = {
            'dob': forms.widgets.DateInput(attrs={'type': 'date'})
        }


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(),required=True)
    
        
        
        