from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class AppleUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=250,widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'Username'})),
    first_name = forms.CharField(max_length=250,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'})),
    last_name = forms.CharField(max_length=250,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'})),
    email = forms.EmailField(max_length=250,widget=forms.EmailInput(attrs={'class':'form-control ','placeholder':'E-mail'})),
    password1 = forms.CharField(max_length=250,widget=forms.PasswordInput(attrs={'class':'form-control ','placeholder':'Password'})),
    password2 = forms.CharField(max_length=250,widget=forms.PasswordInput(attrs={'class':'form-control ','placeholder':'Confirm Password'})),
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']