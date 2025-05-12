from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from store.models import Product  # Assuming you have a Product model in your products app

# View to display the user's cart
@login_required
def cart(request):
    try:
        # Get the cart for the current user
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        # If the user doesn't have a cart, create one
        cart = Cart.objects.create(user=request.user)

    return render(request, 'cart/cart.html', {'cart': cart})

# View to add an item to the cart
@login_required
def add_to_cart(request, product_id):
    if request.method == 'POST':
        try:
            # Get the product based on the provided product_id
            product = Product.objects.get(id=product_id)

            # Get or create the user's cart
            cart, created = Cart.objects.get_or_create(user=request.user)

            # Get or create a cart item for the product in the user's cart
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

            # If the item already exists in the cart, increase its quantity
            if not created:
                cart_item.quantity += 1
                cart_item.save()

            # Return the updated item count in the cart
            return JsonResponse({'count': cart.items.count()})
        except Product.DoesNotExist:
            # If the product doesn't exist, return an error response
            return JsonResponse({'error': 'Product not found'}, status=404)

    # If the request is not POST, return an error
    return JsonResponse({'error': 'Invalid request'}, status=400)
