from django.urls import path
from .views import home_view, item_view  # Make sure to import your view

urlpatterns = [
    path('home/', home_view, name='home'),  # Adjust the path and view as needed
    path('product/<int:product_id>/',  item_view, name='product'),

]