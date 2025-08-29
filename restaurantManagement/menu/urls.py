from django.urls import path
from . import views

app_name = "menuApp"
urlpatterns = [
    path('', views.menu_page, name='menu_page'),
]
