from django.db import models

# Create your models here.
class Product(models.Model):
    # query = models.CharField(max_length=100) for what the user searched for
    name = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=50)
    link = models.URLField(unique=True, blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name    