from django.db import models
from user.models import User
from product.models import Products
# Create your models here.


class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    fname=models.CharField(max_length=150)
    lname=models.CharField(max_length=150)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    address = models.TextField(max_length=200)
    city=models.CharField(max_length=150)
    district=models.CharField(max_length=150)
    state=models.CharField(max_length=150)
    country=models.CharField(max_length=150)
    pin_code=models.IntegerField()
    total_price = models.FloatField()
    payment_mode = models.CharField(max_length=150)
    payment_id=models.CharField(max_length=150,null=True,blank=True)
    order_status = (
        ('pending','pending'),
        ('out for shipping','out for shipping'),
        ('completed','completed'),
        ('canceled','canceled'),
    )
    status = models.CharField(max_length=150,choices=order_status,default='pending')
    message = models.TextField(max_length=500,null=True,blank=True)
    tracking_no = models.CharField(max_length=250,null=True)
    cancel_reason = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}-{}-{}".format(self.fname,self.tracking_no,self.status)
    
    class Meta:
        ordering = ['-created_at']

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity=models.IntegerField(null=False)

    def __str__(self):
        return "{}-{}".format(self.order.id,self.order.tracking_no)


class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    fname=models.CharField(max_length=150)
    lname=models.CharField(max_length=150)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    address = models.TextField(max_length=200)
    city=models.CharField(max_length=150)
    district=models.CharField(max_length=150)
    state=models.CharField(max_length=150)
    country=models.CharField(max_length=150)
    pin_code=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
