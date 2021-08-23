from django.contrib import admin

# Register your models here.
from .models import Bike, Renter, Rental

admin.site.register(Bike)
admin.site.register(Renter)
admin.site.register(Rental)