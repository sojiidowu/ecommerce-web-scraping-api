from django.shortcuts import render
from scraper.jumia_scraper import scrape_jumia_products


# Create your views here.
def home(request):
    products = []
    if request.method == "POST":
        product_name = request.POST.get("product_name")

        products = scrape_jumia_products(product_name)

    return render(request, "core/home.html", {"products": products})