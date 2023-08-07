from django.shortcuts import render,redirect
from django.views import View
from .models  import Category,Products
from cart.models import Cart
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from wishlist.models import Wishlist

@method_decorator(login_required(login_url='welcome'), name='dispatch')
class Category_view(View):
    def get(self,request,slug):
        categories=Category.objects.all() # for navbar
        category=Category.objects.filter(slug=slug) 
        products=Products.objects.filter(category__slug=slug)
        cart=Cart.objects.filter(user=request.user)
        cart_items=cart.count()

        context={'categories':categories,'category':category,'products':products,'cart':cart,'cart_items':cart_items}
        return render(request,'category_view.html',context)

@method_decorator(login_required(login_url='welcome'), name='dispatch')
class Product_view(View):
    def get(self,request,slug):
        categories=Category.objects.all() # for navbar
        products=Products.objects.filter(slug=slug)
        for p in products:
            value=100-(p.offer_price/p.original_price)*100
        offer_per=value

        user_cart=Cart.objects.filter(user=request.user) # for change cart button to go to cart
        sameprod=False
        for prod in user_cart:
           cart_prod_id=prod.product.id
           for p in products:
               prod_id=p.id
               if cart_prod_id == prod_id:
                   sameprod=True
        
        user_wishlist = Wishlist.objects.filter(user=request.user)
        sameitem=False
        for item in user_wishlist:
            wish_prod_id = item.product.id
            for prod in products:
                product_id = prod.id
                if wish_prod_id == product_id:
                    sameitem = True

        cart=Cart.objects.filter(user=request.user)
        cart_items=cart.count()


        context={'products':products,'categories':categories,'offer_per':offer_per,'sameprod':sameprod,'cart':cart,'cart_items':cart_items,'sameitem':sameitem}
        return render(request,'product_view.html',context)

def category_show(request):
    categories=Category.objects.all()
    cart=Cart.objects.filter(user=request.user)
    cart_items=cart.count()
    context={'categories':categories,'cart_items':cart_items,'cart':cart}
    return render(request,'category_show.html',context)