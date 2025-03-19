from django import forms
from taggit.forms import TagWidget 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        labels = {
            "username": "Username",
            "email": "Email Address",
            "password1": "Enter Your Password",
            "password2": "Confirm Your Password",
        }
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class PostForm(forms.ModelForm):
   
    class Meta:
        model = Post
        fields = ('title', 'content', 'tags')
        widgets = {
            'tags': TagWidget(),
        }

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {'content': forms.Textarea(
            attrs={'rows': 5, 
                'cols': 30, 
                'placeholder': 'Enter your comment here...'}
            ),}
        
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content or content.strip() == '':
            raise forms.ValidationError("Comment cannot be empty.")
        return content