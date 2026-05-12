from .models import Product

def save_products(products, query):

    # Delete old results for this query
    Product.objects.filter(query=query).delete()

    saved_count = 0

    for item in products:

        # Basic Validation
        if not item.get("name") or not item.get("link"):
            continue

        # Save to DB
        Product.objects.create(
            query=query,
            name=item.get("name"),
            price=item.get("price", "Unknown"),
            link=item.get("link"),
            image=item.get("image")
        )

        saved_count += 1
        
    return saved_count