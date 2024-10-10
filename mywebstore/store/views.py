from django.shortcuts import render, get_object_or_404, redirect
from store.models import CoffeeProduct, Category, ProductImage, Province, District, Ward
from store.models import Address, Customer, CoffeeProduct, Order, OrderItem
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
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
        print(cart_data) # EXAMPLE: {"27": 2, "28": 3, "29": 9}
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

def checkout(request):
    # Load cart data from cookies (assuming it is stored in cookies)
    cart = json.loads(request.COOKIES.get('cart', '{}'))
    print(cart) # it returns a dictionary, keys are product id, values are quantity of each one
    cart_items = []
    total_cost = 0

    # Example logic to calculate total cost and cart items
    for item_id, quantity in cart.items(): # {'1': 1, '2': 1, '3': 1}, e.g
        product = CoffeeProduct.objects.get(id=item_id)
        item_total = product.cost * quantity
        total_cost += item_total
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'item_total': item_total
        })

    if request.method == 'POST':
        # Handle form submission for placing an order
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        province_id = request.POST.get('province')
        district_id = request.POST.get('district')
        ward_id = request.POST.get('ward')
        address_line = request.POST.get('address-line')

        # Create or update the Customer object
        customer, created = Customer.objects.get_or_create(mobile=mobile, defaults={'name': name})

        # Create the Address object
        ward = Ward.objects.get(id=ward_id)
        address = Address.objects.create(address_line=address_line, ward=ward)

        # Link customer to the new address
        customer.address = address
        customer.save()

        # Create the Order object
        order = Order.objects.create(
            customer=customer,
            address=address,
            total_cost=total_cost
        )

        # Create OrderItems for the order based on the cart data
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                item=item['product'],
                cost=item['item_total'],
                quantity=item['quantity']
            )

        # Clear the cart and redirect to a success page
        # response = redirect('checkout_success')
        # response.delete_cookie('cart')
        # return response

    # Load province, district, and ward options for the form
    provinces = Province.objects.all()
    districts = District.objects.all()
    wards     = Ward.objects.all()

    context = {
        'cart_items': cart_items,
        'total_cost': total_cost,
        'provinces': provinces,
        'districts': districts,
        'wards' : wards,
    }
    # print(request.COOKIES.get('cart')) # {"1": 1, "2": 1, "3": 1}
    # print(cart_items)
    for item in cart_items:
        print(item.keys())
        print(item['product'])
    return render(request, 'store/checkout.html', context)

def load_districts(request):
    province_id = request.GET.get('province_id')
    print(province_id)
    districts = District.objects.filter(province_id=province_id)
    print(districts)
    html = render_to_string('store/partials/district_dropdown_options.html', {'districts': districts})
    return JsonResponse({'html': html})

def load_wards(request):
    district_id = request.GET.get('district_id')
    wards = Ward.objects.filter(district_id=district_id)
    print(wards)
    html = render_to_string('store/partials/ward_dropdown_options.html', {'wards': wards})
    return JsonResponse({'html': html})