from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('<int:product_id>', views.detail, name='detail'),
    path('response/', views.response, name='response'),
    path('<int:product_id>/remove', views.remove, name='remove'),
    path('manage/',views.manage, name='manage'),

]
