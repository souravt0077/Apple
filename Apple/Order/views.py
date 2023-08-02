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
            order_product = Products.objects.filter(id = item.product.id).first()
            order_product.quantity = order_product.quantity - item.quantity
            order_product.save()
        
        cart.delete()
        messages.success(request,'Order confirmed')
        return redirect('home')



        



      

         
































# def place_order(request):
#     if request.method == 'POST':
#         current_user=User.objects.filter(id=request.user.id).first()

#         if not current_user.first_name :
#             current_user.first_name = request.POST.get('fname')
#             current_user.last_name = request.POST.get('lname')
#             current_user.save()

#         if not Profile.objects.filter(user=request.user):
#             userprofile=Profile()
#             userprofile.user = request.user
#             userprofile.fname = request.POST.get('fname')
#             userprofile.lname = request.POST.get('lname')
#             userprofile.email = request.POST.get('email')
#             userprofile.city = request.POST.get('city')
#             userprofile.state = request.POST.get('state')
#             userprofile.pin_code = request.POST.get('pincode')
#             userprofile.phone = request.POST.get('phone')
#             userprofile.district = request.POST.get('district')
#             userprofile.country = request.POST.get('country')
#             userprofile.address = request.POST.get('address')
#             userprofile.save()

#         neworder=Order()
#         neworder.user=request.user
#         neworder.fname=request.POST.get('fname')
#         neworder.email=request.POST.get('email')
#         neworder.city=request.POST.get('city')
#         neworder.state=request.POST.get('state')
#         neworder.pin_code=request.POST.get('pincode')
#         neworder.lname=request.POST.get('lname')
#         neworder.phone=request.POST.get('phone')
#         neworder.district=request.POST.get('district')
#         neworder.country=request.POST.get('country')
#         neworder.message=request.POST.get('message')
#         neworder.address=request.POST.get('address')
#         neworder.payment_mode=request.POST.get('payment_mode')

#         cart_items=Cart.objects.filter(user=request.user)

#         grand_total =0
#         og_total=0
        
#         for item in cart_items:
#             og_price = item.product.original_price * item.quantity
#             og_total = og_total + og_price # total original amount
#             total_price = item.product.offer_price * item.quantity
#             grand_total = grand_total + total_price # total offerd amount
        
#             if grand_total > 50000:
#                 total = grand_total
#             else:
#                 total = grand_total + 40
        
#         neworder.total_price = total

#         trackno=request.user.username + str(random.randint(1111111,9999999))
#         while Order.objects.filter(tracking_no=trackno) is None:
#             trackno=request.user + str(random.randint(1111111,9999999))
        
#         neworder.tracking_no = trackno
#         neworder.save()

#         for item in cart_items:
#             OrderItem.objects.create(
#                 order=neworder,
#                 product=item.product,
#                 price=item.product.offer_price,
#                 quantity=item.quantity
#             )
#             # to reduce the quantity from available stock
#             orderproduct = Products.objects.filter(id=item.product_id).first()
#             orderproduct.quantity = orderproduct.quantity - item.quantity
#             orderproduct.save()
        
#         # clear user cart
#         Cart.objects.filter(user=request.user).delete()
#         messages.success(request,'order has been placed successfully')
#         return redirect('home')
#     return redirect('home')



