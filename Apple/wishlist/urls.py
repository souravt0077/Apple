from django.urls import path
from . import views

urlpatterns = [
    path('add-to-wishlist/',views.add_to_wishlist,name='add-to-wishlist'),
    path('wishlist_show/',views.wishlist_show,name='wishlist_show'),
    path('remove_wishlist/<str:slug>/',views.remove_wishlist,name='remove_wishlist'),
]
