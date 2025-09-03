from django.contrib import admin
from .models import Tables, Reservations

@admin.register(Tables)
class TableAdminRegister(admin.ModelAdmin):
    list_display = ["table_number", 'capacity', 'status', 'seating']
    ordering = ['table_number']
    list_filter = ['capacity', 'status', 'seating']
    actions = ['sets_under_maintanance', 'set_available']

    @admin.action(description='Set status Under Maintanance')
    def set_under_maintanance(self, request, queryset):
        queryset.update(status='U')

    @admin.action(description="Set staus Available")
    def set_available(self, request, queryset):
        queryset.update(status='A')

@admin.register(Reservations)
class ReservationsAdminRegister(admin.ModelAdmin):
    list_display = ['customer_name', 'no_of_guests', 'alloted_table']