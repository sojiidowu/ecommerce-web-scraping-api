from django.db import models

# Create your models here.
class Product(models.Model):
    query = models.CharField(max_length=100) # what the user searched for
    name = models.TextField()
    price = models.CharField(max_length=50)
    link = models.TextField(unique=True)
    image = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name    