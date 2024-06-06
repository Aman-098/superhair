from django.contrib import admin
from services.models import *

# Register your models here.

class ServiceInline(admin.TabularInline):
    model = Service
    extra = 1

class ServiceCategoryAdmin(admin.ModelAdmin):
    inlines = [ServiceInline]

admin.site.register(ServiceCategory, ServiceCategoryAdmin)
admin.site.register(Service)
admin.site.register(Background_content)
