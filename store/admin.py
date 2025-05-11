from django.contrib import admin
from .models import Product, ProductImage, Category, Attribute , AttributeValue, ProductVariant, ProductSpecification, ProductReview, ProductFAQ

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Attribute)
admin.site.register(AttributeValue)
admin.site.register(ProductVariant)
admin.site.register(ProductSpecification)
admin.site.register(ProductReview)
admin.site.register(ProductFAQ)