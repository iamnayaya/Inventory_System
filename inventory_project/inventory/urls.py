# inventory/urls.py

from django.urls import path
from .views import category_list, supplier_list, product_list, product_detail, product_create, product_update, product_delete

urlpatterns = [
    path('categories/', category_list, name='category_list'),
    path('suppliers/', supplier_list, name='supplier_list'),
    path('products/', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('products/create/', product_create, name='product_create'),
    path('products/<int:pk>/update/', product_update, name='product_update'),
    path('products/<int:pk>/delete/', product_delete, name='product_delete'),
    # Add a default path for the root URL
    # You can replace 'product_list' with the appropriate view
    path('', product_list, name='product_list'),
]
