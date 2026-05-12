from core.models import Product

def save_products(products, query):

    # Delete old results for this query
    Product.objects.filter(query=query).delete()

    saved_count = 0

    for item in products:

        # Basic Validation
        if not item.get("name") or not item.get("link"):
            continue

        # Create only if link does not already exist
        product, created = Product.objects.get_or_create(
            link=item.get("link"), # Unique Identifier
            defaults={
                "query": query,
                "name": item.get("name"),
                "price": item.get("price", "Unknown"),
                "image": item.get("image")
            }
        )

        if created:
            saved_count += 1
        
    return saved_count