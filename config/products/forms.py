from django import forms
from .models import Product
class ProductForm(forms.ModelForm):



    class Meta:
        model = Product
        fields = "__all__"

# Then our view will use this form to:

# Add Product
# Edit Product

# without writing repetitive validation logic.