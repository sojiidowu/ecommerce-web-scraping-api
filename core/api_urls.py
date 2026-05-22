from django.urls import path
from .api_views import ProductsListAPIView, scrape_products, task_status

urlpatterns = [
    path('scrape/', scrape_products, name='scrape-products'),
    path('products/', ProductsListAPIView.as_view(), name='product-list'),
    path('task-status/<str:task_id>/', task_status, name ='task-status')
]
