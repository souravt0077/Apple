from django.shortcuts import render,redirect
from . forms import AppleUserCreationForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .models import User
from django.contrib.auth.decorators import login_required

def user_login(request):
    page='Login'
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # try:
        #     User.objects.get(email=email)
        # except:
        #     messages.error(request,'No user found!')
        
        user = authenticate(email=email,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,'Welcome {}'.format(request.user.username))
            return redirect('home')
        else:
            messages.error(request,"Credentials didn't match!")
        

    context={'page':page}
    return render(request,'login_register.html',context)

def user_register(request):
    page = 'Register'
    form=AppleUserCreationForm()
    if request.method == 'POST':
        form=AppleUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.capitalize()
            user.save()
            login(request,user)
            messages.success(request,'Welcome new user {}'.format(request.user.username))
            return redirect('home')
    context={'page':page,'form':form}
    return render(request,'login_register.html',context)

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    messages.success(request,'Sign out successfully')
    return redirect('welcome')

def welcome(request):
    context={}
    return render(request,'login_register.html',context)