from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import run_scraper
from celery.result import AsyncResult

@api_view(['POST'])
def scrape_products(request):
    query = request.data.get('query')

    if not query:
        return Response(
            {"error": "query is required"},
            status=400
        )
    
    # Start background task
    task = run_scraper.delay(query)

    return Response({
        "message": "Scraping started",
        "task_id": task.id,
        "query": query,
    })

class ProductsListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        query = self.request.query_params.get("query")

        if query:
            return Product.objects.filter(query=query).order_by("-created_at")
        
        return Product.objects.none()
    
@api_view(['GET'])
def task_status(request, task_id):
    task = AsyncResult(task_id)

    return Response({
        "task_id": task.id,
        "status": task.status,
        "result": task.result if task.ready() else None
    })