from django.urls import path
from . import views

urlpatterns = [
    path('',views.cart,name='cart'),
    path('<int:product_id>/add',views.add,name='add'),
    path('<int:remove_id>/remove_cart',views.remove_cart,name='remove_cart'),
]
