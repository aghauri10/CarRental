from django.db import models
from django.contrib.auth.models import User
import uuid 

class Customer(models.Model):
    occupation_choices = [('Student','Student'),('Unemployed','Unemployed'),('Employed','Employed')]
    gender_choices = [('M','Male'),('F','Female'),('X','Prefer Not to Say')]

    user = models.OneToOneField(User,on_delete=models.CASCADE) 
    gender = models.CharField(blank = False,choices = gender_choices,max_length = 50)
    dob = models.DateField(blank = False)
    occupation = models.CharField(blank = True,choices = occupation_choices,max_length = 50,default = 'Unemployed')
    phone_number = models.CharField(blank = False,max_length = 15)
    license_number = models.CharField(max_length = 50)
    
    def __str__(self):
        return str(self.user.username) + '_'  + str(self.license_number)

class Car(models.Model):
    car_id = models.UUIDField(primary_key = True,default = uuid.uuid4)
    brand = models.CharField(max_length = 50)
    model = models.CharField(max_length = 50)
    year = models.CharField(max_length = 4)
    color = models.CharField(max_length = 50)
    mileage = models.IntegerField()
    car_number = models.CharField(max_length = 25)
    image = models.ImageField(upload_to = './images/car/')
    price = models.IntegerField()
    
    
class Reviews(models.Model):
    review_id = models.UUIDField(primary_key = True,default = uuid.uuid4)
    car_id = models.ForeignKey(Car,on_delete=models.CASCADE)
    user_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    rating = models.IntegerField(choices = [(0.0, '0.0'), (0.5, '0.5'), (1.0, '1.0'), (1.5, '1.5'), (2.0, '2.0'), (2.5, '2.5'), (3.0, '3.0'), (3.5, '3.5'), (4.0, '4.0'), (4.5, '4.5'), (5.0, '5.0')],default = 0)
    description = models.CharField(max_length=250)
    reviewed_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        unique_together = ('car_id','user_id')