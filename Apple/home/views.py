from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from product.models import Category
from cart.models import Cart
from django.utils.decorators import method_decorator
from django.views import View

@method_decorator(login_required(login_url='welcome'), name='dispatch')
class Home(View):
    def get(self,request):
        categories=Category.objects.all()
        cart=Cart.objects.filter(user=request.user)
        cart_items=cart.count()
        context={'categories':categories,'cart_items':cart_items}
        return render(request,'home.html',context)

