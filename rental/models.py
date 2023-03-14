from django.db import models
from django.contrib.auth.models import User
import uuid 
from .validators import year_validator
from django.core.validators import MinValueValidator,MaxValueValidator
#uuid is used to create random id, its an external package not related to django


class Customer(models.Model):
    occupation_choices = [('Student','Student'),('Unemployed','Unemployed'),('Employed','Employed')]
    gender_choices = [('Male','Male'),('Female','Female'),('Prefer Not to Say','Prefer Not to Say')]
    

    user = models.OneToOneField(User,on_delete=models.CASCADE) 
    profile_pic = models.ImageField(upload_to="images/customer",default="images/customer/default.png")
    gender = models.CharField(blank = False,choices = gender_choices,max_length = 50)
    dob = models.DateField(blank = False)
    occupation = models.CharField(blank = True,choices = occupation_choices,max_length = 50,default = 'Unemployed')
    phone_number = models.CharField(blank = False,max_length = 15)
    license_number = models.CharField(max_length = 50)
    last_modified = models.DateTimeField(blank = True,auto_now=True)
    
    def __str__(self):
        return str(self.user.username) + '_'  + str(self.license_number)

class Car(models.Model):
    # choices needs to be stored in list of tuples where each tuple takes format of (value to store in db,value to display)
    brand_choices = [('Ford', 'Ford'), ('Vauxhall', 'Vauxhall'), ('Volkswagen', 'Volkswagen'), ('BMW', 'BMW'), ('Audi', 'Audi'), ('Mercedes-Benz', 'Mercedes-Benz'), ('Toyota', 'Toyota'), ('Nissan', 'Nissan'), ('Peugeot', 'Peugeot'), ('Renault', 'Renault'),('Other','Other')]
    color_choices = [('White', 'White'), ('Black', 'Black'), ('Grey', 'Grey'), ('Silver', 'Silver'), ('Blue', 'Blue'), ('Red', 'Red'), ('Brown', 'Brown'), ('Green', 'Green'), ('Orange', 'Orange'), ('Purple', 'Purple'), ('Beige', 'Beige'), ('Purple', 'Purple'), ('Gold', 'Gold'), ('Yellow', 'Yellow')]
    
    car_id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable=False)
    brand = models.CharField(max_length = 50,blank = False,choices = brand_choices)
    model = models.CharField(max_length = 50,blank = False)
    year = models.PositiveSmallIntegerField(validators=[year_validator],blank = False)
    color = models.CharField(max_length = 50,blank = False,choices = color_choices)
    mileage = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(200000)])
    car_number = models.CharField(max_length = 25,unique=True)
    image = models.ImageField(upload_to = 'images/car',default='images/car/default.jpeg')
    price = models.IntegerField(validators=[MinValueValidator(0)],blank=False)
    description = models.CharField(max_length=1000,blank = True)
    is_available = models.BooleanField(default=True)
    last_modified = models.DateTimeField(blank = True,auto_now=True)
    
    def __str__(self):
        return f"{str(self.brand)}-{str(self.model)}-{(str(self.year))}-{str(self.car_number)}" 

class RentHistory(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    car = models.ForeignKey(Car,on_delete=models.SET_NULL,null=True)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    damage_description = models.TextField(default="To be filled by system when car returned")
    rented_at = models.DateTimeField(auto_now_add=True)
    returned_at = models.DateTimeField(blank = True,null = True)
    
    def __str__(self):
        return f"{str(self.car)} by {str(self.customer)} on {str(self.rented_at)}"
    
class Reviews(models.Model):
    review_id = models.UUIDField(primary_key = True,default = uuid.uuid4)
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    rating = models.IntegerField(choices = [(0.0, '0.0'), (1.0, '1.0'), (2.0, '2.0'), (3.0, '3.0'), (4.0, '4.0'), (5.0, '5.0')],blank = False)
    description = models.CharField(max_length=250)
    reviewed_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        unique_together = ('customer','car')