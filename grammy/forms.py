from .models import Post, Comment,Profile
from django import forms

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user']

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user']

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
