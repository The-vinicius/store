from django import forms
from products.models import Category

class CategoryForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        max_length=100,
        required=True,
    )
    image = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={"class": "d-none", "onchange": "image_select();"}
        )
    )

    class Meta:
        model = Category
        fields = ('name', 'image')
