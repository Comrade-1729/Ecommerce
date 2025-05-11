# cart/views.py
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem

@login_required
def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        return JsonResponse({'count': cart.items.count()})
    return JsonResponse({'error': 'Invalid request'}, status=400)