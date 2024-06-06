from django.contrib import admin
from book.models import *

# Register your models here.

class BookAppointmentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'appointment_date', 'appointment_time')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('appointment_date', 'appointment_time', 'like_website', 'find_us')

admin.site.register(Book_Appointment, BookAppointmentAdmin)
admin.site.register(Background_Images)
admin.site.register(Body_Content)
