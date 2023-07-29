from django.urls import path
from . import views

urlpatterns = [
    path('add-to-cart/',views.add_to_cart,name='add-to-cart'),
    path('cart',views.Cart_view.as_view(),name='cart'),
]
