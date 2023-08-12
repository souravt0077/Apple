from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import JsonResponse
from product.models import Products
from .models import Wishlist
from product.models import Category
from cart.models import Cart
from django.http import HttpResponseRedirect
from django.urls import reverse
# from django.db.models import Q

def add_to_wishlist(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = request.POST.get('id')
            prod_ckeck = Products.objects.get(id = prod_id)
            
            if prod_ckeck:
                if Wishlist.objects.filter(product_id=prod_id).filter(user=request.user):
                    return JsonResponse({"status":"Allready in wishlist"})
                else:
                    Wishlist.objects.create(
                        user=request.user,
                        product=prod_ckeck
                    )
                    return JsonResponse({"status":"Wishlist created"})
            else:
                return JsonResponse({"status":"No product found !"})
        else:
            return JsonResponse({'status':'Login to continue'})
    
    return redirect('home')

def wishlist_show(request):
    wishlist=Wishlist.objects.filter(user=request.user.id)
    categories=Category.objects.all() # for navbar
    cart=Cart.objects.filter(user=request.user)

    same_prod = False
    for item in wishlist:
        wish_prod=item.product.id
        for ci in cart:
            cart_prod = ci.product.id
            if wish_prod == cart_prod:
                same_prod = True
    
    context={'wishlist':wishlist,'categories':categories,'same_prod':same_prod}
    return render(request,'wishlist.html',context)

# def remove_wishlist(request,pk):
#     wishlist=Wishlist.objects.filter(user=request.user).filter(id=pk).first()
#     wishlist.delete()
#     messages.success(request,'{} ({}) removed from wishlist'.format(wishlist.product.name,wishlist.product.varient))
#     return redirect('wishlist_show')

def remove_wishlist(request,slug):
    product = Products.objects.get(slug=slug)
    wishlist=Wishlist.objects.filter(user=request.user).filter(product=product)
    wishlist.delete()
    messages.success(request,'{} ({}) removed from wishlist'.format(product.name,product.varient))
    return HttpResponseRedirect(reverse('product_view',args=[slug]))