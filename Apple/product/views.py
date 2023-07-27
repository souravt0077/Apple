from django.shortcuts import render,redirect
from django.views import View
from .models  import Category,Products

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
        context={'products':products,'categories':categories}
        return render(request,'product_view.html',context)
