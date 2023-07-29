from django.shortcuts import render,redirect
from django.views import View
from django.http import JsonResponse
from product.models import Products
from .models import Cart

# Create your views here.

class Cart_view(View):
    def get(self,request):
        context={}
        return render(request,'cart.html',context)

def add_to_cart(request):
    if request.method == 'POST': #checking the request is POST or not
        
        if request.user.is_authenticated: # checking the user is authenticated or not
            prod_id=request.POST.get('id') # getting the product id
            prod_check = Products.objects.get(id=prod_id) # checking the id have any product exist 

            if prod_check:
                qty=request.POST.get('qty') #getting the quantity enterd bythe user

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
