from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField

# Category Model (Hierarchical)
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='categories/', blank=True)
    featured = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

# Product Model (Electrical Appliances)
class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sku = models.CharField(max_length=50, unique=True)  # Stock Keeping Unit
    brand = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    
    # Electrical Specifications
    voltage = models.CharField(max_length=20, blank=True)  # e.g., "220V"
    wattage = models.PositiveIntegerField(blank=True, null=True)  # e.g., "1500W"
    power_source = models.CharField(max_length=50, blank=True, choices=[('AC', 'AC'), ('DC', 'DC'), ('BATTERY', 'Battery')])
    safety_certifications = models.CharField(max_length=200, blank=True, help_text="e.g., UL, CE, RoHS")
    
    # Warranty & Support
    warranty_period = models.CharField(max_length=50, blank=True)  # e.g., "2 years"
    warranty_type = models.CharField(max_length=50, blank=True, choices=[('MANUFACTURER', 'Manufacturer'), ('SELLER', 'Seller')])
    
    # Descriptions
    short_description = models.TextField(blank=True)
    long_description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    thumbnail = CloudinaryField('image', folder='products/thumbnails')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    @property
    def is_on_sale(self):
        return self.discount_price is not None and self.discount_price < self.price

# Product Images
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')
    alt_text = models.CharField(max_length=100, blank=True)
    is_feature = models.BooleanField(default=False)

    def __str__(self):
        return f"Image for {self.product.name}"

# Attributes & Variants
class Attribute(models.Model):
    name = models.CharField(max_length=100, unique=True)  # e.g., "Color"
    description = models.TextField(blank=True)

class AttributeValue(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=100)  # e.g., "Red"

class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    attribute_values = models.ManyToManyField(AttributeValue)
    sku = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)

# Technical Specifications
class ProductSpecification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='specifications')
    key = models.CharField(max_length=100)  # e.g., "Weight"
    value = models.CharField(max_length=100)  # e.g., "5 kg"

# Reviews & FAQs
class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True)
    is_approved = models.BooleanField(default=False)

class ProductFAQ(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='faqs')
    question = models.CharField(max_length=200)
    answer = models.TextField()