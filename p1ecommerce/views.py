from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from cart.forms import CartAddProductForm
from django.db.models import Q

def product_list(request, category_slug=None):
    queryset = request.GET.get('buscar')
    if queryset:
        products = Product.objects.filter(
            Q(name__icontains=queryset),
            Q(description__icontains=queryset)
        ).distinct()

    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category,
                                     slug= category_slug )
        products= products.filter(category=category)

    return render(request,
                      'tienda/products/list.html',
                      {'category': category,
                       'categories': categories,
                       'products': products})


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
