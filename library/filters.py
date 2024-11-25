# library/filters.py
import django_filters
from .models import Book, Category

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Title')
    author = django_filters.CharFilter(lookup_expr='icontains', label='Author')
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all(), label='Category')
    publication_date = django_filters.DateFromToRangeFilter(label='Publication Date Range')

    class Meta:
        model = Book
        fields = ['title', 'author', 'category', 'publication_date']
