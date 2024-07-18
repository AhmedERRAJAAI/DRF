from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price = models.DecimalField(null=False, default=0, decimal_places=2, max_digits=10)
    
    def __str__(self) -> str:
        return f"{self.title}"
    
    @property
    def get_sale_price(self):
        pass