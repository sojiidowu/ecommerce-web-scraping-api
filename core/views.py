from django.shortcuts import render
from scraper.jumia_scraper import scrape_jumia_products
from .services import save_products
from .models import Product


# Create your views here.
def home(request):
    product_name = None
    if request.method == "POST":
        product_name = request.POST.get("product_name")

        products = scrape_jumia_products(product_name)

        saved = save_products(products, product_name)

        print(f"{saved} new products saved!")

    # products = Product.objects.all().order_by("-created_at")
    products = Product.objects.filter(query=product_name).order_by("-created_at")

    return render(request, "core/home.html", {"products": products})