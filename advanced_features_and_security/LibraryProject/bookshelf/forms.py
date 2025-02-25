from django import forms
from .models import Book

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=200, required=True, help_text="Enter the book title")
    author = forms.CharField(max_length=100, required=True, help_text="Enter the author's name")

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author"]
