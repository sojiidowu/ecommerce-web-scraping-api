import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_scraper_endpoint_return_success():
    # 1. Arrange: Create an API client and prepare the URL & patload
    client = APIClient()

    url = reverse('product-list')
    payload = {
        "url": "http://127.0.0.1:8000/api/products/?query=laptop"
    }

    # 2. Act: Make a POST request to your API
    response = client.get(url, payload, format='json') # type: ignore

    # 3. Assert: Verify the API responds with the correct status code
    assert response.status_code == status.HTTP_200_OK