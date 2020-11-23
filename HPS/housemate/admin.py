from django.contrib import admin
from .models import *

#Register the models here

admin.site.register(User)
admin.site.register(Landlord)
admin.site.register(ShareProfile)
admin.site.register(RentalProperty)
admin.site.register(SaleProperty)
admin.site.register(ShareProperty)
#admin.site.register(Advertisement)
#admin.site.register(Media)
admin.site.register(Property)