from django.db import models
from django.conf import settings
from timeless.models import Product


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    stripe_payment_intent = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return str(self.id)
    
