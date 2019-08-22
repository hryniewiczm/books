from django.urls import path
from . import views
from . import forms

app_name = 'book'

urlpatterns = [
    path('books_list/', views.BookListView.as_view(), name='BookListView'),
    path('book_created/', views.BookCreateForm, name='BookCreateForm' ),
]