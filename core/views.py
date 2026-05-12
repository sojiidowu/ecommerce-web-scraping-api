from django.shortcuts import render
from .models import Product
from .product_query_service import get_products_for_query


# Create your views here.
def home(request):
    products = Product.objects.none()

    if request.method == "POST":
        product_name = request.POST.get("product_name")

        products = get_products_for_query(product_name)

    return render(request, "core/home.html", {"products": products})