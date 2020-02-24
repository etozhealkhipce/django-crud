from django import forms
from .models import *

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title','body', 'slug']

class TagForm(forms.ModelForm):
	class Meta:
		model = Tag
		fields = ['name']

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['body']