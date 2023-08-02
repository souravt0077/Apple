from django.forms import ModelForm
from .models import Cart

class Cartform(ModelForm):
    class Meta:
        model = Cart
        fields = "__all__"