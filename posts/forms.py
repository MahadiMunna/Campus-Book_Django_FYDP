from django import forms
from .models import PostModel

class PostForm(forms.ModelForm):
    class Meta:
        model=PostModel
        fields= ['post','book_name','book_author','book_image','post_type']