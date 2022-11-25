from django import forms
from products.models import Category

class CategoryForm(forms.ModelForm):
    image = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={"class": "d-none", "onchange": "image_select();"}
        )
    )

    class Meta:
        model = Category
        fields = ('name', 'image')
