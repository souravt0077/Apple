from django.urls import path
from . import views


urlpatterns = [
    path('place_order/',views.place_order,name='place_order'),
    path('my_orders/',views.my_orders,name='my_orders'),
    path('canceling_order/<str:pk>/',views.canceling_order,name='canceling_order'),
    path('canceled_order/<str:pk>/',views.canceled_order,name='canceled_order'),
    path('view_order/<str:pk>/',views.view_order,name='view_order'),
    path('order_history/',views.order_history,name='order_history'),

]
