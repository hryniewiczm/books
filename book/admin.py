from django.contrib import admin

from .models import Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name',]
    list_filter = ['name',]
    search_fields = ['name',]

admin.site.register(Author, AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'authors', 'published',]
    list_filter = ['title', 'authors', 'publishedDate',]
    search_fields = ['title', 'authors', 'publishedDate',]

admin.site.register(Book, BookAdmin)
