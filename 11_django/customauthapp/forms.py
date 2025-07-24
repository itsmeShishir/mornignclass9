from django import forms
from blog.models import Tag, Category

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title']

class CategoryForm(forms.Form):
    class Meta:
        model = Category
        fields = ['title', 'img']