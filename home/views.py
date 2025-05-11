from django.shortcuts import render
from store.models import Category, Product

def home(request):
    context = {
        'featured_categories': Category.objects.filter(featured=True)[:4],
        'featured_products': Product.objects.filter(featured=True)[:4],
        'cart_items_count': request.cart.items.count() if hasattr(request, 'cart') else 0
    }
    return render(request, 'home.html', context)