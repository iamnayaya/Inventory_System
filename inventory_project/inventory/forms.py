# inventory/forms.py

from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category',
                  'supplier', 'quantity', 'price']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        # Add Bootstrap classes to form fields for styling
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
