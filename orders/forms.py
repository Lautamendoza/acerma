from django import forms
from .models import Order
from django.utils.translation import gettext_lazy as _

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'paid']
        labels = {
            'first_name': _("Nombre"),
            'last_name': _("Apellido"),
            'email': _("Correo Electrónico"),
            'address': _("Dirección"),
            'postal_code': _("Código Postal"),
            'city': _("Ciudad"),
            'created': _("Creado"),
            'paid': _("Pagado"),

        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Tu nombre')}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Tu apellido')}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': _('Tu correo electrónico')}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Tu dirección')}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Tu código postal')}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Tu ciudad')}),
         }