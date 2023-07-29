from django.shortcuts import render,redirect
from django.views import View
from .models  import Category,Products
from cart.models import Cart

class Category_view(View):
    def get(self,request,slug):
        categories=Category.objects.all() # for navbar
        category=Category.objects.filter(slug=slug) 
        products=Products.objects.filter(category__slug=slug)

        context={'categories':categories,'category':category,'products':products}
        return render(request,'category_view.html',context)

class Product_view(View):
    def get(self,request,slug):
        categories=Category.objects.all() # for navbar
        products=Products.objects.filter(slug=slug)
        for p in products:
            value=(p.offer_price/p.original_price)
        offer_per=100-value*100

        user_cart=Cart.objects.filter(user=request.user)
        sameprod=False
        for prod in user_cart:
           cart_prod_id=prod.product.id
           for p in products:
               prod_id=p.id
               if cart_prod_id == prod_id:
                   sameprod=True

        
        context={'products':products,'categories':categories,'offer_per':offer_per,'sameprod':sameprod}
        return render(request,'product_view.html',context)