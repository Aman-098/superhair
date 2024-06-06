from django.contrib import admin
from contact.models import*

# Register your models here.


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email','comments','timestamp')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('email','comments')

admin.site.register(ContactFormSubmission,ContactFormAdmin)

admin.site.register(Contact_Background)
admin.site.register(ContactInfo)
admin.site.register(Body)


