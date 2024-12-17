from django.urls import path

from .views import products_view, product_details_view

app_name = 'products';
urlpatterns = [
    path("products/", products_view, name="products_view"),
    path("products/details/<int:product_id>", product_details_view, name="product_details_view"),
]