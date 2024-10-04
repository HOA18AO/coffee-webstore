from django.shortcuts import render, get_object_or_404, redirect
from store.models import CoffeeProduct, Category, ProductImage
from django.http import HttpResponse, JsonResponse
import json

# Create your views here.
def home_view(request):
    categories = Category.objects.all()  # Get all categories
    
    category_id = request.GET.get('category')
    if category_id:
        products = CoffeeProduct.objects.filter(category_id=int(category_id))
    else:
        products = CoffeeProduct.objects.all()
    
    for product in products:
        product.image = ProductImage.objects.get(product=product, is_main=True).image
        # get 1 image (main image), "attach additional data (like the image) to each product dynamically"
        # this did not add another field to product model

    context = {
        'products': products, # including an extra item, the main image
        'categories': categories,
    }

    return render(request, 'store/home.html', context)

def item_view(request, product_id):
    # return render(request, 'store/product.html')
    product = get_object_or_404(CoffeeProduct, pk=product_id)
    categories = Category.objects.all()
    product_images = ProductImage.objects.filter(product=product)
    # Assuming a related Image model or list in the Product model
    return render(request, 'store/product.html', {
        'product': product,
        'categories': categories,
        'product_images': product_images
    })

def add_to_cart(request, product_id):
    if request.method == 'POST':
        cart = request.COOKIES.get('cart')
        
        if cart:
            cart = json.loads(cart)
        else:
            cart = {}

        if str(product_id) in cart:
            cart[str(product_id)] += 1
        else:
            cart[str(product_id)] = 1

        cart_data = json.dumps(cart)
        
        response = JsonResponse({
            'success': True,
            'cart_count': sum(cart.values())  # Send back the total number of items in the cart
        })
        response.set_cookie('cart', cart_data, max_age=60*60*24*1)  # 1 day
        return response

    return JsonResponse({'success': False}, status=405)

def remove_from_cart(request, product_id):
    # print('removing')
    if request.method == 'POST':
        cart = request.COOKIES.get('cart', '{}')

        try:
            cart = json.loads(cart)  # Load the cart from cookies
        except json.JSONDecodeError:
            cart = {}
        # Remove the item from the cart
        if str(product_id) in cart:
            del cart[str(product_id)]
        print(f'product {product_id} has been removed')
        # Update the cookie
        response = JsonResponse({'success': True})
        response.set_cookie('cart', json.dumps(cart), max_age=3600)  # Update the cookie with the modified cart
        return response
    print(request.COOKIES.get('cart'))
    return JsonResponse({'success': False})

# def update_cart_quantity(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         product_id = str(data.get('product_id'))
#         new_quantity = int(data.get('quantity'))
#         print(f'{product_id}')
#         # Get cart from cookies
#         cart = request.COOKIES.get('cart', {})
        
#         if product_id in cart:
#             # cart[product_id]['quantity'] = new_quantity
#             cart[product_id] = new_quantity

#         # print(cart)
#         # Update the cookie
#         response = JsonResponse({'success': True})
#         response.set_cookie('cart', cart)
#         print(request.COOKIES.get('cart'))
#         return response

#     return JsonResponse({'success': False})

def update_cart_quantity(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = str(data.get('product_id'))  # Ensure product_id is a string
        new_quantity = int(data.get('quantity'))  # Ensure new_quantity is an integer
        # print(f'Updating product {product_id} to quantity {new_quantity}') # EXAMPLE: Updating product 29 to quantity 9

        # Get cart from cookies and deserialize it into a Python dictionary
        cart = request.COOKIES.get('cart', '{}')  # Default to an empty JSON object if 'cart' is not found
        cart = json.loads(cart)  # Convert the cart from a JSON string to a Python dictionary

        # Check if the product is in the cart and update its quantity
        if product_id in cart:
            cart[product_id] = new_quantity

        # Serialize the updated cart back to a JSON string
        cart_data = json.dumps(cart)

        # Update the cookie with the modified cart
        response = JsonResponse({'success': True})
        response.set_cookie('cart', cart_data, max_age=60*60*24*1)  # 1 day
        # print(cart_data) # EXAMPLE: {"27": 2, "28": 3, "29": 9}
        # print(request.COOKIES.get('cart')) # EXAMPLE: {"27": 2, "28": 3, "29": 8} # because the respone.set_cookie() DOES NOT update the cookie imidiately, so everything is good
        return response

    return JsonResponse({'success': False})

def cart_view(request):
    # Get the cart from cookies (if it exists), otherwise initialize an empty cart
    cart = request.COOKIES.get('cart')
    print(cart)
    if cart:
        # Deserialize the cart from JSON string to Python dictionary
        cart = json.loads(cart)
    else:
        cart = {}

    # Get the product information for the items in the cart
    product_ids = cart.keys()
    products = CoffeeProduct.objects.filter(id__in=product_ids)
    # print(products)
    # Calculate the total cost
    total_bill = 0
    for product in products:
        quantity = cart[str(product.id)]
        product.quantity = quantity
        product.total_cost = product.cost  * quantity
        total_bill += product.total_cost

    context = {
        'cart': cart,
        'items': products,
        'total_bill': total_bill,
    }
    # print(cart)

    return render(request, 'store/cart.html', context)