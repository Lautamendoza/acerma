from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    class Meta:

        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]

    def __str__(self):
            return self.name
    
    def get_absolute_url(self):
     return reverse('tienda:product_list_by_category',
                    args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, 
                                related_name='products',
                                on_delete=models.CASCADE)
    name= models.CharField(max_length=200)
    slug= models.SlugField(max_length=200)
    image= models.ImageField(upload_to='products/%Y/%m/%d',
                            blank=True)
    description= models.TextField(blank=True)
    price = models.DecimalField(max_digits=5,
                                decimal_places=2)
    available= models.BooleanField(default=True)
    created= models.DateTimeField(auto_now=True)
    updated= models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering= ['name']

    def __str__(self):
            return self.name
        
    def get_absolute_url(self):
           return reverse('tienda:product_detail',
                    args=[self.id, self.slug])   