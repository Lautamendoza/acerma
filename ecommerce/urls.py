from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/',include ('cart.urls', namespace='cartt')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('',include ('p1ecommerce.urls', namespace='tienda')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)