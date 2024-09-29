from django.contrib import admin

# Register your models here.
# from django.contrib import admin
from .models import City, District, Address, Customer, Category, CoffeeProduct, ProductImage, Order, OrderItem, Payment, Delivery

admin.site.register(City)
admin.site.register(District)
admin.site.register(Address)
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(CoffeeProduct)
admin.site.register(ProductImage)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(Delivery)
