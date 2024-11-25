# library/models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    published_date = models.DateField()

    def __str__(self):
        return self.title
