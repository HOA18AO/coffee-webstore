from django.urls import path
from .views import home_view, item_view, cart_view, add_to_cart, remove_from_cart, update_cart_quantity  # Make sure to import your view
from .views import checkout, load_districts, load_wards

urlpatterns = [
    path('home/', home_view, name='home'),  # Adjust the path and view as needed
    path('product/<int:product_id>/',  item_view, name='product'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('update_cart_quantity/', update_cart_quantity, name='update_cart_quantity'),
    path('cart/', cart_view, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('load_districts/', load_districts, name='load_districts'),
    path('load_wards/', load_wards, name='load_wards'),
]