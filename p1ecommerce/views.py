from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from cart.forms import CartAddProductForm
from django.db.models import Q


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    query = request.GET.get('search') 
    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    return render(request, 'tienda/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })

    
    


def product_detail(request, id, slug):
    product= get_object_or_404(Product,
                               id = id,
                               slug = slug,
                               available = True)
    cart_product_form= CartAddProductForm()
    
    return render(request,
                  'tienda/products/detail.html',
                  {'product': product,
                  'cart_product_form': cart_product_form })

def formas_de_pago(request):
    return render(request, 'tienda/formaspago.html')

def envios(request):
    return render(request, 'tienda/envios.html')

def cambiosyd(request):
    return render(request, 'tienda/cambiosyd.html')

def preguntas(request):
    return render(request, 'tienda/preguntas.html')

def nosotros(request):
    return render(request, 'tienda/nosotros.html')

def cart_details(request):
    return render(request, 'cart/details.html')

def hormigon(request):
    return render(request, 'tienda/hormigon.html')
