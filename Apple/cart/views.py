from django.shortcuts import render,redirect
from django.views import View
from django.http import JsonResponse 
from product.models import Products
from .models import Cart
from product.models import Category
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required(login_url='welcome'), name='dispatch')
class Cart_view(View):
    def get(self,request):
        cart=Cart.objects.filter(user=request.user)
        cart_items=cart.count()
        categories=Category.objects.all() # for navbar
        

        context={'cart':cart,'categories':categories,'cart_items':cart_items}
        return render(request,'cart.html',context)

@login_required(login_url='welcome')
def add_to_cart(request):
    if request.method == 'POST': #checking the request is POST or not
        
        if request.user.is_authenticated: # checking the user is authenticated or not
            prod_id=request.POST.get('id') # getting the product id
            prod_check = Products.objects.get(id=prod_id) # checking the id have any product exist 

            if prod_check:
                qty=request.POST.get('qty') #getting the quantity enterd bythe user

                if prod_check.quantity == 0:
                    return JsonResponse({"status":"Out of stock"})

                if Cart.objects.filter(product_id=prod_id,user=request.user): # checking the product is already in the cart or not
                    return JsonResponse({"status":"Product allready in cart"})
                else:
                    Cart.objects.create( # if product is not exist in the cart then creating a new cart item
                        user=request.user,
                        product=prod_check,
                        quantity=qty
                    )
                    return JsonResponse({"status":"Product added to Cart "})
            else:
                return JsonResponse({"status":"No Product found!"})
        else:
            return JsonResponse({"status":"Login to continue"})
    return redirect('home')


def delete_all_cart(request):
    cart=Cart.objects.filter(user=request.user)
    cart.delete()
    return redirect('cart')

# def delete_cart(request,pk):
#     pass
