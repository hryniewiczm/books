from django import forms
from .models import Book, Author


class BookCreateForm(forms.Form):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publishedDate', 'industryIndentifiers',
                  'pageCount', 'imageLinks', 'language']