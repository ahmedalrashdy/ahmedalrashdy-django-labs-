from django.urls import path
from .views import CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDetailView, CategoryDeleteView
from . import views
app_name="products"
urlpatterns = [
    path('', CategoryListView.as_view(), name='category-list'),
    path('new/', CategoryCreateView.as_view(), name='category-create'),
    path('<int:pk>/edit/', CategoryUpdateView.as_view(), name='category-update'),
    path('<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
     path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/create/', views.product_create, name='product-create'),
    path('products/<int:pk>/edit/', views.product_update, name='product-update'),
    path('products/<int:pk>/delete/', views.product_delete, name='product-delete'),
]
