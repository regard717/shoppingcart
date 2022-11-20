"""shoppingcart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.good_index, name='index'),
    path('cart/', views.cart_index, name="cart"),
    path('cart_add/<vlist_id>', views.cart_add, name="cart_add"),
    path('check_out/', views.check_out, name="check_out"),
    path('askdelete/<clist_CartGoodsName>', views.askdelete, name="askdelete"),
    path('manager/', views.manager, name="manager"),
    path('manager/plusQuantity/<vlist_GoodsName>', views.plusQuantity, name="plusQuantity"),
    path('manager/minusQuantity/<vlist_GoodsName>', views.minusQuantity, name="minusQuantity"),
    path('manager/deleteGoods/<vlist_GoodsName>', views.deleteGoods, name="deleteGoods"),
    path('manager/shipping/<slist_SoldGoodsName>', views.shipping, name="shipping"),
    path('add_function/', views.add_function, name="add_function"),
]
