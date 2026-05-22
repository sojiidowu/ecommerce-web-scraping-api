from celery import shared_task
from .product_query_service import get_products_for_query

@shared_task
def run_scraper(query):
    result = get_products_for_query(query)
    return {"query": query, "count": len(result)}