from .models import Post, Comment,Profile,Follow
from django import forms

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user']

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'comments',
            'user',
            'post'
        ]

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class NewFollowForm(forms.ModelForm):
    class Meta:
        model = Follow
        # exclude = set()
        exclude = ['user']

