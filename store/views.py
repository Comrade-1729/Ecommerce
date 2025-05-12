# store/views.py

import os
from django.shortcuts import render, get_object_or_404
from meilisearch import Client
from .models import Product

def product_list(request):
    """
    Display a list of all available products.
    """
    products = Product.objects.filter(is_available=True)
    return render(request, 'store/product_list.html', {'products': products})


def product_detail(request, slug):
    """
    Display a single product’s detail page.
    """
    product = get_object_or_404(Product, slug=slug, is_available=True)
    return render(request, 'store/product_detail.html', {'product': product})


def search(request):
    """
    Perform a MeiliSearch query on the 'products' index.
    """
    query = request.GET.get('q', '')
    client = Client(
        os.getenv('MEILISEARCH_URL'),
        os.getenv('MEILISEARCH_MASTER_KEY')
    )
    results = client.index('products').search(query, {
        'attributesToRetrieve': ['id','name', 'slug', 'price', 'thumbnail'],
        'limit': 10
    })
    # results['hits'] is a list of dicts with keys matching attributesToRetrieve
    return render(request, 'search/results.html', {'results': results['hits']})
