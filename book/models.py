from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=250)
    authors = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='Authors')
    publishedDate = models.DateField(verbose_name='publishedDates')
    industryIndentifiers = models.CharField(max_length=250)
    pageCount = models.PositiveIntegerField()
    imageLinks = models.URLField(verbose_name='imagesLinks')
    language = models.CharField(max_length=2)

    def published(self):
        return self.publishedDate.strftime('%Y')

    class Meta:
        ordering = ['title', 'authors', 'publishedDate']

    def __str__(self):
        return self.title
