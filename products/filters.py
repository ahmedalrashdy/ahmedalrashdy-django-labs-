from django_filters import rest_framework as filters
from django.db.models import Q
from .models import Product

class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains", label="اسم المنتج")
    buy_price = filters.RangeFilter(field_name="buy_price", label="سعر الشراء (من-إلى)")
    sell_price = filters.RangeFilter(field_name="sell_price", label="سعر البيع (من-إلى)")
    discount = filters.RangeFilter(field_name="discount", label="نسبة الخصم (من-إلى)")
    qty = filters.RangeFilter(field_name="qty", label="الكمية (من-إلى)")
    category = filters.CharFilter(field_name="category__name", lookup_expr="icontains", label="اسم التصنيف")
    has_discount = filters.BooleanFilter(method='filter_has_discount', label="منتجات بخصومات فقط")

    def filter_has_discount(self, queryset, name, value):
        if value is True: 
            return queryset.filter(discount__gt=0)
        elif value is False:
            return queryset.filter(discount=0)
        return queryset  

    class Meta:
        model = Product
        fields = ['name', 'buy_price', 'sell_price', 'discount', 'qty', 'category', 'has_discount']
