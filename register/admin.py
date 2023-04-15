from django.contrib import admin
from .models import Appointment, Option, Stylist, Address
# Register your models here.
admin.site.register(Appointment)
admin.site.register(Option)
admin.site.register(Stylist)
admin.site.register(Address)
