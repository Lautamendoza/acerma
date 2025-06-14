from django import forms
from django.utils.translation import gettext_lazy as _

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]

class CartAddProductForm(forms.Form):
    cantidad = forms.TypedChoiceField(
        label=_("Cantidad"),
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int
    )

    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )
