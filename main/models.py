import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.PositiveIntegerField(default=0) # Jumlah stok produk yang tersedia
    origin = models.CharField(max_length=100, blank=True, null=True)  # Asal produk (dari daerah mana)
    rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)


