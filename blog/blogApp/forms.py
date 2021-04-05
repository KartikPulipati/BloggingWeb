from django import forms
from django.contrib.auth.models import User
from .models import blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = ['title', 'blog']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'blog': forms.Textarea(attrs={'class': 'form-control'}),


        }