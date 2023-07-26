from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from product.models import Category

@login_required(login_url='login')
def home(request):
    categories=Category.objects.all()
    context={'categories':categories}
    return render(request,'home.html',context)
