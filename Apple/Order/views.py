from django.shortcuts import render,redirect
from user.models import User
from .models import Profile,Order,OrderItem
from cart.models import Cart
from product.models import Products
import random
from django.contrib import messages


def place_order(request):
    if request.method == 'POST':
        user=User.objects.filter(id=request.user.id).first()
        
        if not user.first_name: # filling the firstname and last name column of User model if it is empty
            user.first_name = request.POST.get('fname')
            user.last_name = request.POST.get('lname')
            user.save()

        if not Profile.objects.filter(user=request.user): # creating a new profile if it is not exist
            user_profile = Profile()
            user_profile.user = request.user.username
            user_profile.fname = request.POST.get('fname')
            user_profile.email = request.POST.get('email')
            user_profile.city = request.POST.get('city')
            user_profile.city = request.POST.get('state')
            user_profile.pin_code = request.POST.get('pincode')
            user_profile.lname = request.POST.get('lname')
            user_profile.phone = request.POST.get('phone')
            user_profile.district = request.POST.get('district')
            user_profile.country = request.POST.get('country')
            user_profile.address = request.POST.get('address')
            user_profile.save()

        new_order = Order() # adding order details

        new_order.user = request.user
        new_order.fname = request.POST.get('fname')
        new_order.email = request.POST.get('email')
        new_order.city = request.POST.get('city')
        new_order.city = request.POST.get('state')
        new_order.pin_code = request.POST.get('pincode')
        new_order.lname = request.POST.get('lname')
        new_order.phone = request.POST.get('phone')
        new_order.district = request.POST.get('district')
        new_order.country = request.POST.get('country')
        new_order.address = request.POST.get('address')
        new_order.payment_mode = request.POST.get('payment_mode')
        new_order.message = request.POST.get('message')

        cart=Cart.objects.filter(user=request.user) #filtering cart items of the user

        grand_total =0
        og_total=0
    
        for item in cart:
            og_price = item.product.original_price * item.quantity
            og_total = og_total + og_price # total original amount
            total_price = item.product.offer_price * item.quantity
            grand_total = grand_total + total_price # total offerd amount
    
            if grand_total > 50000: # checking the amount greater than 50 k 
                total = grand_total 
            else:
                total = grand_total + 40 # if amount is lessthan 50 k then add 40rs for shipping charge

            # checking the product quantity is not lessthan the cart quantity
            if not item.product.quantity >= item.quantity:
                messages.error(request,"Can't add to cart. Insufitient quantity please check the quantity of the product ...  ")
                return redirect('cart')
            
        new_order.total_price = total 

        tranckno = request.user.username + str(random.randint(1111111,9999999))

        while Order.objects.filter(tracking_no=tranckno) is None :
            tranckno = request.user.username + str(random.randint(1111111,9999999))
        
        new_order.tracking_no = tranckno
        new_order.save()


        for item in cart: 
            OrderItem.objects.create( # creating order items through filtering from request.user cart
                order = new_order,
                product = item.product,
                price= item.product.offer_price,
                quantity = item.quantity
            )
            # removing cart quantity from product
            order_product = Products.objects.filter(id = item.product.id).first() 
            order_product.quantity = order_product.quantity - item.quantity 
            order_product.save()

        # clearing the cart products
        cart.delete()
        messages.success(request,'Order confirmed')
        return redirect('home')

def my_orders(request):
    orders=Order.objects.filter(user=request.user)[:3]
    order=False
    for item in orders:
        if item.status == 'pending' or item.status == 'out for shipping':
            order=True
            break
        break
    cart = Cart.objects.filter(user=request.user)
    context={'orders':orders,'order':order,'cart':cart}
    return render(request,'myorders.html',context)


def canceling_order(request,pk):
    order=Order.objects.get(id=pk)
    context={'order':order}
    return render(request,'cancel_order.html',context)

def canceled_order(request,pk):
    order=Order.objects.get(id=pk)
    order.status = 'canceled'
    order.save()
    order_items=OrderItem.objects.filter(order=order)
    for item in order_items:
        product=Products.objects.filter(id=item.product_id).first()
        product.quantity = product.quantity + item.quantity
        product.save()
    
    messages.success(request,'Order Canceled')
    return redirect('my_orders')

def view_order(request,pk):
    orders=Order.objects.get(id=pk)
    order_items=OrderItem.objects.filter(order__id=orders.id)
    context={'orders':orders,'order_items':order_items}
    return render(request,'view_order.html',context)

def order_history(request):
    orders=Order.objects.filter(user=request.user)
    context={'orders':orders}
    return render(request,'order_history.html',context)
        



      

         


















