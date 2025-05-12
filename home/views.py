from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import Category, Product

def home(request):
    context = {
        'featured_categories': Category.objects.filter(featured=True)[:4],
        'featured_products': Product.objects.filter(featured=True)[:4],
        'cart_items_count': request.cart.items.count() if hasattr(request, 'cart') else 0
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Add logic to save the email (e.g., to a database)
        messages.success(request, 'Thanks for subscribing!')
        return redirect('home')  # Redirect to the home page
    return redirect('home')  # Handle GET requests by redirecting