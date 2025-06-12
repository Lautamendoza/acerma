from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from cart.forms import CartAddProductForm
from django.db.models import Q
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User     
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

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

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('tienda:product_list')
        else:
            return render(request, 'login_register.html', {'error': 'Credenciales incorrectas'})

    return render(request, 'login_register.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return render(request, 'login_register.html', {'error': 'Las contraseñas no coinciden'})

        if User.objects.filter(username=username).exists():
            return render(request, 'login_register.html', {'error': 'El usuario ya existe'})

        user = User.objects.create_user(username=username, email=email, password=password1)
        auth_login(request, user)
        return redirect('/')

    return render(request, 'login_register.html')
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu cuenta fue creada. Ahora puedes iniciar sesión.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'login_register.html', {'register_form': form})
















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
