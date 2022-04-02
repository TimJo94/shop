from django import forms
from .models import Product, Comment


class CreateProductForm(forms.ModelForm):
    name = forms.CharField()
    class Meta:
        model = Product
        # fields = ('name', 'description', 'category', 'price', 'image')
        fields = '__all__'


class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('__all__')
