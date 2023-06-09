from django import forms

from .models import *


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'created_by']


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'content', 'created_by']


class CommentUpdateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'content']


class ReplyCreateForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['comment', 'content', 'created_by']


class ReplyUpdateForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['comment', 'content']
