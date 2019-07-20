from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product,Response
from django.utils import timezone
from cart.models import Cart
from django.http import JsonResponse
from django.template.loader import render_to_string

def home(request):
    products = Product.objects.all()
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
    return render(request, 'products/home.html',{'products':products,'choices':choices})

@login_required
def create(request):
    if request.method == 'POST':
        product = Product()
        product.title = request.POST['title']
        product.body = request.POST['body']
        product.icon = request.FILES['icon']
        product.image = request.FILES['image']
        product.url = request.POST['url']
        if product.url.startswith('http://') or product.url.startswith('https://'):
            pass
        else:
            product.url = 'http://' + product.url

        product.pub_date = timezone.datetime.now()
        product.hunter = request.user
        product.body = request.POST['body']

        product.save()
        return redirect('/products/' + str(product.id))

    else:
        return render(request,'products/create.html')


def detail(request, product_id):
    product = get_object_or_404(Product, pk = product_id)
    product.likes = len(Response.objects.filter(lproduct=product,choice='like'))
    product.dislikes = len(Response.objects.filter(lproduct=product,choice='dislike'))
    product.save()
    try:
        res=Response.objects.get(lproduct=product,user=request.user).choice
    except:
        res='none'
    choices={product.id:res}
    return render(request, 'products/detail.html', {'product':product,'choices':choices})


#@login_required(login_url='/accounts/signup')
@login_required
def response(request):
    product_id = request.POST.get('id')
    choice = request.POST.get('choice')
    product = get_object_or_404(Product, pk = product_id)
    try:
        res = Response.objects.get(lproduct=product,user=request.user)
        if res.choice==choice:
            res.choice  = 'none'
        else:
            res.choice  = choice
        res.save()
    except:
        Response.objects.create(user=request.user,lproduct=product,choice=choice)
    finally:
        product.likes = len(Response.objects.filter(lproduct=product,choice='like'))
        product.dislikes = len(Response.objects.filter(lproduct=product,choice='dislike'))
        product.save()
    #return redirect('/products/' + str(product.id))
    # return redirect('/')
   
    choices={}
    try:
        res=Response.objects.get(lproduct=product,user=request.user).choice
    except:
            res='none'
    choices.update({product.id:res})
    if request.is_ajax():
        html = render_to_string('like.html',{'product':product,'choices':choices},request=request)
        return JsonResponse({'form':html})

@login_required
def manage(request):
    return render(request,'products/manage.html',{'products':Product.objects.filter(hunter=request.user)})

@login_required
def remove(request,product_id):
    get_object_or_404(Product,pk=product_id).delete()
    try:
        objs = Cart.objects.filter(product_id=product_id)
        for obj in objs:
            obj.delete()
    finally:
        return redirect('manage')
