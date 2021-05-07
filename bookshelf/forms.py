from django import forms
from .models import Book, Author

class NewBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author']

# class AdoptDogForm(forms.ModelForm):
#     class Meta:
#         model = Dog
#         fields = ['owner']
#         widgets = {'owner': forms.HiddenInput()}