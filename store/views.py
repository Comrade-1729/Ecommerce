from django.shortcuts import render
from .models import Product
from meilisearch import Client

def search(request):
    query = request.GET.get('q', '')
    client = Client(os.getenv('MEILISEARCH_URL'), os.getenv('MEILISEARCH_MASTER_KEY'))
    results = client.index('products').search(query, {
        'attributesToRetrieve': ['name', 'slug', 'price', 'thumbnail'],
        'limit': 10
    })
    return render(request, 'search/results.html', {'results': results['hits']})