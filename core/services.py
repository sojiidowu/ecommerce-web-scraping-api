from .models import Product

def save_products(products):
    saved_count = 0

    for item in products:

        # Basic Validation
        if not item.get("name") or not item.get("link"):
            continue

        # Save to DB
        product, created = Product.objects.get_or_create(
            link=item["link"], # Duplication Unique Identifier
            defaults={
                "name": item.get("name"),
                "price": item.get("price", "Unknown"),
                "image": item.get("image")
            }
        )

        if created:
            saved_count += 1
        
    return saved_count