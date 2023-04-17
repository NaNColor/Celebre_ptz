from django.contrib import admin
from .models import Appointment, Option, Stylist, Address, Times, Blocks, WorkSchedule
# Register your models here.
class WorkScheduleAdmin(admin.ModelAdmin):
    list_display = ('stylist', 'day_of_work', )
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'proof', )
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Option)
admin.site.register(Stylist)
admin.site.register(Address)
admin.site.register(Times)
admin.site.register(WorkSchedule, WorkScheduleAdmin)
admin.site.register(Blocks)
