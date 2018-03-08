from .models import Post, Comments
from django import forms

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user']

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['user']