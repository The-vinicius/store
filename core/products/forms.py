from django import forms
from django.forms import inlineformset_factory
from .models import Product, Category, ImageProduct

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


# custom widget
class CustomClearableFileInput(forms.ClearableFileInput):
    template_name = 'widgets/customclearablefileinput.html'


class ImageForm(forms.ModelForm):
    photo = forms.ImageField(
        widget=CustomClearableFileInput(attrs={"class":"d-none"})
    )
    class Meta:
        model = ImageProduct
        fields = ('photo',)


# formset to update imageprodut
ImageProductFormset = inlineformset_factory(
    Product,
    ImageProduct,
    form=ImageForm,
    extra=0,
    can_delete=False,
    min_num=0,
    validate_min=True,
    fields=('photo',)
)
