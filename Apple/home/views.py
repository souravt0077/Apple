from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from product.models import Category
from cart.models import Cart
from django.utils.decorators import method_decorator
from django.views import View
from Order.models import OrderItem,Order
from wishlist.models import Wishlist

@method_decorator(login_required(login_url='welcome'), name='dispatch')
class Home(View):
    def get(self,request):
        categories=Category.objects.all()
        cart=Cart.objects.filter(user=request.user)
        cart_items=cart.count()
        orders=Order.objects.filter(user=request.user)
        order=False
        for item in orders:
            if item.status == 'pending' or item.status == 'out for shipping':
                order=True
                break
            break
        
        wishlist=Wishlist.objects.filter(user=request.user)
        wishlist_count=wishlist.count()

        context={'categories':categories,'cart_items':cart_items,'cart':cart,'order':order,'wishlist':wishlist,'wishlist_count':wishlist_count}
        return render(request,'home.html',context)

