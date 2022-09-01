from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple':True}))
    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'price', 'is_available', 'image')
