from django.contrib import admin
from .models import Product,Response

admin.site.register(Product)
admin.site.register(Response)

# admin.site.register(Pizza)
# admin.site.register(Topping)
# admin.site.register(ToppingAmount)