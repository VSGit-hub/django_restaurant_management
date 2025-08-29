from django.shortcuts import render
from django.http import HttpResponse
from .models import ItemCategory

def menu_page(request):
    categories = ItemCategory.objects.prefetch_related('item_category').all()
    context = {'categories':categories}
    return render(request, 'menu/menupage.html', context)
