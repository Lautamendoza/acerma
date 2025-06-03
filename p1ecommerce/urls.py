from django.urls import path
from . import views

app_name= 'tienda'

urlpatterns = [
   path('formas-de-pago/', views.formas_de_pago, name='formas_de_pago'),
  path ('envios/', views.envios, name='envios'),
  path ('cambiosyd/', views.cambiosyd, name='cambiosyd'),
  path ('preguntas/', views.preguntas, name='preguntas'),
  path ('nosotros/', views.nosotros, name='nosotros'),
  path('', views.product_list, name='product_list'),
  path('<int:id>/<slug:slug>/', views.product_detail, name= 'product_detail'),
  path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
]