from django import forms
from .models import Blog

class CommentForm(forms.Form):
    commenter_name = forms.CharField(label = "Name:", max_length = 100)
    email = forms.CharField(label = "Email:", max_length = 100)
    content = forms.CharField(label = "Comment", max_length = 1000)
