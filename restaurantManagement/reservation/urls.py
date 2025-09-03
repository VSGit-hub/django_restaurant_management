from django.urls import path
from . import views

app_name = 'reservationApp'
urlpatterns = [
    path('reserve_table/', views.reserve_table, name='reserve_table'),
    path('success/', views.booking_success, name='booking_success')
]   
