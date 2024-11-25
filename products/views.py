import os
from .filters import ProductFilter
from django_filters.views import FilterView
from django.contrib import messages
from .forms import ProductForm
from .models import Product
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Category
from .forms import CategoryForm


class CategoryListView(ListView):
    model = Category
    template_name = 'categories/category_list.html'
    context_object_name = 'categories'


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/category_form.html'
    success_url = reverse_lazy('products:category-list')

    def form_valid(self, form):
        return super().form_valid(form)


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/category_form.html'
    success_url = reverse_lazy('products:category-list')

    def form_valid(self, form):
        return super().form_valid(form)


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'categories/category_detail.html'
    context_object_name = 'category'


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'categories/category_confirm_delete.html'
    context_object_name = 'category'
    success_url = reverse_lazy('products:category-list')

    def delete(self, request, *args, **kwargs):
        category = self.get_object()
        return super().delete(request, *args, **kwargs)



class ProductListView(FilterView):
    template_name = "products/product_list.html"
    filterset_class = ProductFilter
    queryset = Product.objects.all()


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "تم إضافة المنتج بنجاح.")
            return redirect('products:product-list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form})


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "تم تعديل المنتج بنجاح.")
            return redirect('products:product-list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', {'form': form, 'product': product})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, "تم حذف المنتج بنجاح.")
        return redirect('products:product-list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})