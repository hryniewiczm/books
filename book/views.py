from django.shortcuts import render
from django.views.generic import ListView, CreateView

from .forms import BookCreateForm
from .models import Author, Book


class BookListView(ListView):
    model = Book
    template_name = "book/books_list.html"

# def book_create(request):
#     book = Book(request)
#     if request.method == 'POST':
#         form = BookCreateForm(request.POST)
#         if form.is_valid():
#             order = form.save()
#             for item in book:
#                 Book.objects.create(order=order,
#                                         product=item['product'],
#                                         price=item['price'],
#                                         quantity=item['quantity'])
#             # clear the cart
#             book.clear()
#             return render(request,
#                           self.template_name)
#
#     else:
#         form = BookCreateForm()
#     return render(request,
#                   'books/book_create.html',
#                   {'book': book, 'form': form})