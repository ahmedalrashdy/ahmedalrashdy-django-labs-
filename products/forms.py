from django import forms
from .models import Category, Product

from django import template




class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'image']
        labels = {
            'name': 'اسم الفئة',
            'image': 'صورة الفئة',
        }
        error_messages = {
            'name': {
                'required': 'يرجى إدخال اسم الفئة',
                'unique': 'اسم الفئة موجود بالفعل، يرجى اختيار اسم آخر',
                'max_length': 'اسم الفئة يجب أن لا يتجاوز 100 حرف',
            },
            'image': {
                'invalid': 'يرجى تحميل صورة صحيحة',
            },
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'discount', 'image', 'category', 'qty', 'buy_price', 'sell_price']
        labels = {
            'name': 'اسم المنتج',
            'discount': 'نسبة الخصم',
            'image': 'صورة المنتج',
            'category': 'الفئة',
            'qty': 'الكمية',
            'buy_price': 'سعر الشراء',
            'sell_price': 'سعر البيع',
        }
        error_messages = {
            'name': {
                'required': 'يرجى إدخال اسم المنتج',
                'max_length': 'اسم المنتج يجب أن لا يتجاوز 255 حرف',
            },
            'discount': {
                'required': 'يرجى إدخال نسبة الخصم',
                'invalid': 'يرجى إدخال نسبة خصم صحيحة',
                'max_digits': 'نسبة الخصم يجب أن لا تتجاوز 5 أرقام',
                'decimal_places': 'نسبة الخصم يجب أن لا تتجاوز خانتين عشريتين',
            },
            'image': {
                'invalid': 'يرجى تحميل صورة صحيحة',
            },
            'category': {
                'required': 'يرجى اختيار الفئة',
            },
            'qty': {
                'required': 'يرجى إدخال الكمية',
                'invalid': 'يرجى إدخال كمية صحيحة',
            },
            'buy_price': {
                'required': 'يرجى إدخال سعر الشراء',
                'invalid': 'يرجى إدخال سعر شراء صحيح',
                'max_digits': 'سعر الشراء يجب أن لا يتجاوز 10 أرقام',
                'decimal_places': 'سعر الشراء يجب أن لا يتجاوز خانتين عشريتين',
            },
            'sell_price': {
                'required': 'يرجى إدخال سعر البيع',
                'invalid': 'يرجى إدخال سعر بيع صحيح',
                'max_digits': 'سعر البيع يجب أن لا يتجاوز 10 أرقام',
                'decimal_places': 'سعر البيع يجب أن لا يتجاوز خانتين عشريتين',
            },
        }
