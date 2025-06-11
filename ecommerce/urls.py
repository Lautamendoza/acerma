from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from p1ecommerce import views
from django.contrib.auth.views import LogoutView
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('cart/',include ('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('',include ('p1ecommerce.urls', namespace='tienda')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'p1ecommerce', 'static'))