from django.db import models
from suppliers.models import Supplier
from products.models import Product



class Inflow(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, related_name='inflow')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='inflow')
    quantity = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.product)
