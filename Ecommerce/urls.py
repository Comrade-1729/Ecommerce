from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('users/', include('users.urls')),
    path('orders/', include('orders.urls')),
    path('store/', include('store.urls')),
]
