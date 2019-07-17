from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from products.models import Product

class Cart(models.Model):
    product_id = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        product = get_object_or_404(Product,pk=self.product_id)
        return product.title
