from django.shortcuts import render
from django.views.generic import ListView, CreateView

from .forms import BookCreateForm
from .models import Author, Book


class BookListView(ListView):
    queryset = Book.objects.order_by('-publishedDate')
    model = Book
    paginate_by = 3
    template_name = "book/books_list.html"

class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'authors', 'publishedDate', 'industryIndentifiers', 'pageCount', 'imageLinks', 'language']
    template_name = "book/book_created.html"
    success_url = 'book/books_list.html'

# dsf