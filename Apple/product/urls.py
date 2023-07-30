from django.urls import path
from . import views

urlpatterns = [
    path('category_view/<str:slug>/',views.Category_view.as_view(),name='category_view'),
    path('product_view/<str:slug>/',views.Product_view.as_view(),name='product_view'),
    path('category_show/',views.category_show,name='category_show'),
]
