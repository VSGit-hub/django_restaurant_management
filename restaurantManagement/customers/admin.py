from django.contrib import admin
from .models import CustomerProfile

@admin.register(CustomerProfile)
class CustomerProfileAdminRegister(admin.ModelAdmin):
    list_display = ['name', 'phone']
    
