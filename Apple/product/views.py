from django.shortcuts import render,redirect
from django.views import View
from .models  import Category,Products,Likes
from cart.models import Cart
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from wishlist.models import Wishlist
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


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
        
        offer_per = 0
        for p in products:
            value=100-(p.offer_price/p.original_price)*100 #calculating discount percentage
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

        # like btn change
        product=Products.objects.get(slug=slug)
        like = Likes.objects.filter(user=request.user,product=product)
        total_likes = Likes.objects.filter(product=product).count()
        total_likes -=1

        if like:
            like_icon = True
        else:
            like_icon = False

        context={'products':products,'categories':categories,'sameprod':sameprod,'offer_per':offer_per,'cart':cart,'cart_items':cart_items,'sameitem':sameitem,'like_icon':like_icon,'total_likes':total_likes}
        return render(request,'product_view.html',context)

def category_show(request):
    categories=Category.objects.all()
    cart=Cart.objects.filter(user=request.user)
    cart_items=cart.count()
    context={'categories':categories,'cart_items':cart_items,'cart':cart}
    return render(request,'category_show.html',context)

class search_show(View):
    def get(self,request):
        search=str(request.GET.get('search'))
        products= Products.objects.filter(Q(name__icontains=search) | Q(varient__icontains=search))
        context={'products':products}
        return render(request,'search.html',context)
    
def like(request,slug):
    user = request.user
    product = Products.objects.get(slug=slug)
    current_likes = product.likes
    liked = Likes.objects.filter(user=user,product=product)

    if not liked:
        liked = Likes.objects.create(
            user=user,
            product=product
        )
        current_likes += 1
        messages.success(request,'Product Liked')
    else:
        liked = Likes.objects.filter(user=user,product=product).delete()
        current_likes -= 1
        messages.success(request,'Product Unliked')

    product.likes = current_likes
    product.save()
    return HttpResponseRedirect(reverse('product_view',args=[slug]))

def liked_products_show(request):
    categories=Category.objects.all() # for navbar
    liked = Likes.objects.filter(user=request.user)

    context={'liked':liked,'categories':categories}
    return render(request,'liked_products.html',context)