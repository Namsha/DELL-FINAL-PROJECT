from django import forms
from biashara.models import Product


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'origin', 'color']


