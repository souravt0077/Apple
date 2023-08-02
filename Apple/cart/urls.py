from django.urls import path
from . import views

urlpatterns = [
    path('add-to-cart/',views.add_to_cart,name='add-to-cart'),
    path('cart',views.Cart_view.as_view(),name='cart'),
    path('delete_all_cart/',views.delete_all_cart,name='delete_all_cart'),
    path('delete_cart/<str:pk>/',views.delete_cart,name='delete_cart'),

    # checkout
    path('checkout_view/',views.Checkout_view,name='checkout_view'),
]
