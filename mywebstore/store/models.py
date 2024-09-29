from django.db import models

class City(models.Model):
    city_name = models.CharField(max_length=30)

    def __str__(self):
        return self.city_name

class District(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    district_name = models.CharField(max_length=30)

    def __str__(self):
        return self.district_name

class Address(models.Model):
    address_line = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.address_line

class Customer(models.Model):
    CUSTOMER_TYPE = [
        ('guest', 'Guest'),
        ('register', 'Register')
    ]
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('private', 'Private')
    ]

    type = models.CharField(max_length=10, choices=CUSTOMER_TYPE, default='guest')
    password = models.CharField(max_length=255, blank=True, null=True)  # optional for registered users
    mobile = models.CharField(max_length=11)
    email = models.EmailField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name

class CoffeeProduct(models.Model):
    PRODUCT_STATUS = [
        ('available', 'Available'),
        ('unavailable', 'Unavailable')
    ]
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    unit = models.CharField(max_length=30, blank=True, null=True)  # e.g., 'gói 250g', 'gói 500g'
    status = models.CharField(max_length=15, choices=PRODUCT_STATUS, default='available')
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description_short = models.CharField(max_length=200, blank=True, null=True)
    description_long = models.TextField(blank=True, null=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

class ProductImage(models.Model):
    product = models.ForeignKey(CoffeeProduct, on_delete=models.CASCADE)
    image = models.URLField(max_length=100, default='https://placehold.co/1200x750')
    is_main = models.BooleanField(default=False)

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ]

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='pending')

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(CoffeeProduct, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    class Meta:
        unique_together = ('order', 'item')

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('online', 'Online'),
        ('cash', 'Cash')
    ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    payment_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('done', 'Done')], default='pending')

    def __str__(self):
        return f"Payment for Order {self.order.id}"

class Delivery(models.Model):
    DELIVERY_STATUS = [
        ('received', 'Received'),
        ('not_received', 'Not Received')
    ]
    
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    delivery_method = models.CharField(max_length=50)  # e.g., DIY, Shopee, etc.
    received_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=15, choices=DELIVERY_STATUS)

    def __str__(self):
        return f"Delivery for Order {self.order.id}"
