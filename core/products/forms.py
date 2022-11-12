from django import forms

from .models import Product, Category


class ProductForm(forms.ModelForm):
    image = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={"multiple": True, "class": "d-none", "onchange": "image_select();"}
        )
    )
    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        max_length=100,
        required=True,
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control"}),
        max_length=500,
        required=True,
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    class Meta:
        model = Product
        fields = ("name", "description", "category", "price", "is_available", "image")
