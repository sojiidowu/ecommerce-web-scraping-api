from django.urls import path
from .api_views import ProductsListAPIView, scrape_products

urlpatterns = [
    path('scrape/', scrape_products, name='scrape-products'),
    path('products/', ProductsListAPIView.as_view(), name='product-list'),
]
