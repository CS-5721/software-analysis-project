from django.db import models

# User Tabel
class User(models.Model):
    username = models.CharField(max_length=50, unique=True) 
    email = models.CharField(max_length=255)  #default null=False equivalent of NOT NULL
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=60)

    def __str__(self): 
        return self.username

#Share Profiles
class ShareProfile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    #Not sure who to map the habits: smoking, drinking, Pet
    habits = models.CharField(max_length=150)
    likes = models.CharField(max_length=150)
    dislikes = models.CharField(max_length=150)

#Landlord profile
class Landlord(User):
    ll_username = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        primary_key=True, 
        related_name='+'
    )
    rtb_id = models.IntegerField()

    def __str__(self):
        return self.ll_username


#property 
class Property(models.Model):
    #id is a primary key here by default
    owner_username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    address = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.owner_username

#Rental Property
class RentalProperty(Property):
    rental_id = models.ForeignKey(Property, on_delete=models.CASCADE, primary_key=True, related_name='+')
    rent = models.IntegerField()

#Sale property
class SaleProperty(Property):
    sale_id = models.ForeignKey(Property, on_delete=models.CASCADE, primary_key=True, related_name='+')
    price = models.IntegerField()

#Share Property
class ShareProperty(Property):
    RENT_TYPE = (
        ('W', 'Weekly'),
        ('M', 'Monthly'),
    )
    share_id = models.ForeignKey(Property, on_delete=models.CASCADE, primary_key=True, related_name='+')
    rent = models.IntegerField()
    rent_type = models.CharField(max_length=1, choices=RENT_TYPE)

#Advertisement
class Advertisement(models.Model):
    adv_id = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='+',
        primary_key=True
    )

class Media(models.Model):
    advt_id = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='+')
    TYPE = (
        ('P', 'Photos'),
        ('V', 'Videos'),
        ('O', 'Other'),
    )
    #How this to be int not char?
    media_type = models.CharField(max_length=1, choices=TYPE)
    location = models.CharField(max_length=100)