from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", include('home.urls')),
    path('', RedirectView.as_view(url='home/' )),
    path('menu/', include('menu.urls')),
    path('reserve/', include('reservation.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
