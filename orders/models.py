from django.db import models
from p1ecommerce.models import Product


class Order(models.Model):
    first_name = models.CharField("Nombre", max_length=50)
    last_name = models.CharField("Apellido", max_length=50)
    email = models.EmailField("Correo electrónico")
    address = models.CharField("Dirección", max_length=250)
    postal_code = models.CharField("Código postal", max_length=20)
    city = models.CharField("Ciudad", max_length=100)
    paid = models.BooleanField("Pagado", default=False)
    created = models.DateTimeField("Creado", auto_now_add=True)
    def __str__(self):
        return f"Orden de {self.first_name} {self.last_name}"

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['created'])
        ]

    def __str__(self):
        return f'Order {self.id} '
    

class OrderItem(models.Model):
    order= models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5,
                                decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
