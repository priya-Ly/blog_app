from django import forms
from .models import BlogPost,Comment

class BlogPostForm(forms.ModelForm):
    class Meta:
        model=BlogPost
        fields=('blog_title','blog_content')
        exclude=['published_date']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
