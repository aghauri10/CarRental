from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    gender_choices = [('M','Male'),('F','Female'),('X','Prefer Not to Say')]

    user = models.OneToOneField(User,on_delete=models.CASCADE) 
    profile_pic = models.ImageField(upload_to="images/employee",default="images/employee/default.png")
    gender = models.CharField(blank = False,choices = gender_choices,max_length = 50)
    dob = models.DateField(blank = False)
    phone_number = models.CharField(blank = False,max_length = 15)
    company_number = models.CharField(max_length = 50)
    last_modified = models.DateTimeField(blank = True,auto_now=True)
    
    def __str__(self):
        return str(self.user.username) + '_'  + str(self.company_number)