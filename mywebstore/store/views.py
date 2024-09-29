from django.shortcuts import render, get_object_or_404
from store.models import CoffeeProduct, Category, ProductImage

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
    # print(product_images)
    for image in product_images:
        print(image.image) # prints the url of the image
    return render(request, 'store/product.html', {
        'product': product,
        'categories': categories,
        'product_images': product_images
    })

