from django import forms

from .models import Post

class TextForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'post'
        ]
