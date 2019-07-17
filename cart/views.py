from django.shortcuts import render,redirect,get_object_or_404
from .models import Cart
from products.models import Product,Response
from django.contrib.auth.decorators import login_required

@login_required
def cart(request):
    products = []
    cart_items = Cart.objects.filter(user=request.user)
    for item in cart_items:
        products.append(get_object_or_404(Product,pk=item.product_id))
    choices={}
    for product in products:
        product.likes = len(Response.objects.filter(lproduct=product,choice='like'))
        product.dislikes = len(Response.objects.filter(lproduct=product,choice='dislike'))
        product.save()
        try:
            res=Response.objects.get(lproduct=product,user=request.user).choice
        except:
            res='none'
        choices.update({product.id:res})
    return render(request,'cart/cart.html',{'products':products,'choices':choices})

@login_required
def add(request,product_id):
    try:
        Cart.objects.get(product_id=product_id,user=request.user)
    except:
        cart_item = Cart()
        cart_item.user = request.user
        cart_item.product_id = product_id
        cart_item.save()
    return redirect('home')

@login_required
def remove_cart(request,remove_id):
    Cart.objects.get(user=request.user,product_id=remove_id).delete()
    return redirect('cart')