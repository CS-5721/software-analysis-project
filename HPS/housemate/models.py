from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from housemate.hps_logger import *
logger = Logger.instance()

logger.log("Initialising model")

# User Table
class User(models.Model):
    username = models.CharField(max_length=50, unique=True) 
    email = models.EmailField(max_length=75)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=60)

    def __str__(self): 
        return self.username

#Habits traits
class Habits(models.Model):
    traits = models.CharField(max_length=50) 
    
    def __str__(self):
        return self.traits
    
#Share Profiles
class ShareProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='+')
    #Not sure who to map the habits: smoking, drinking, Pet
    habits = models.ManyToManyField(Habits)
    likes = models.CharField(max_length=150, null=True)
    dislikes = models.CharField(max_length=150, null=True)

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='+')
    gender=models.CharField(max_length=6,choices=(('Male','Male'),('Female','Female'),))
    phone=models.IntegerField(default=0)
    date_of_birth=models.DateField("DOB",help_text="YYYY-MM-DD",blank=True,null=True)

    def __unicode__(self):
        return '{} Profile'.format(self.user) #removed self.user.username
     
#Landlord profile
class Landlord(models.Model):
    uname = models.OneToOneField(User, on_delete=models.CASCADE, related_name='+', unique=True)
    rtb_id = models.IntegerField(unique=True, null=False)

    def __str__(self):
        return self.uname


#property 
class Property(models.Model):
    #id is a primary key here by default
    ownername = models.ForeignKey(Landlord, on_delete=models.CASCADE, related_name='+')
    address = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.ownername

#Rental Property
class RentalProperty(models.Model):
    rentID = models.OneToOneField(Property, on_delete=models.CASCADE, related_name='+')
    RENT_TYPE = (
        ('W', 'Weekly'),
        ('M', 'Monthly'),
    )
    rent = models.IntegerField()
    rent_type = models.CharField(max_length=1, choices=RENT_TYPE, default='M')

#Sale property
class SaleProperty(models.Model):
    saleID = models.OneToOneField(Property, on_delete=models.CASCADE, related_name='+')
    price = models.IntegerField()


#Share Property
class ShareProperty(models.Model):
    shareID = models.OneToOneField(RentalProperty, on_delete=models.CASCADE, related_name='+')
    shareProfileID = models.OneToOneField(ShareProfile, on_delete=models.CASCADE, related_name='+',null=True)


#Advertisement
class Advertisement(models.Model):
    property_id = models.OneToOneField(Property, on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return self.property_id

class Media(models.Model):
    adv_id = models.OneToOneField(Advertisement, on_delete=models.CASCADE, related_name='+', unique=True)
    TYPE = (
        ('P', 'Photos'),
        ('V', 'Videos'),
        ('O', 'Other'),
    )
    media_type = models.CharField(max_length=1, choices=TYPE)
    filename = models.FileField(upload_to='media/')

    def __str__(self):
        return self.media_type
