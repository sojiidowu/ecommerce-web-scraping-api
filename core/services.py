from .models import Product

def save_products(products):
    saved_count = 0

    for item in products:

        # Save to DB
        product, created = Product.objects.get_or_create(
            link=item["link"], # duplication unique identifier
            defaults={
                "name": item["name"],
                "price": item["price"],
                "image": item["image"]
            }
        )

        if created:
            saved_count += 1
    
    return saved_count