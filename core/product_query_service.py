from scraper.jumia_scraper import scrape_jumia_products
from .services import save_products
from .models import Product
import logging

logger = logging.getLogger(__name__)

def get_products_for_query(query):

    scraped_products = scrape_jumia_products(query)
    saved = save_products(scraped_products, query)
    logger.info(f"{saved} new products saved!")

    return Product.objects.filter(query=query).order_by("-created_at")
