from django.db.models import Sum
from django.shortcuts import render
from .models import Good, Cart, Sold

# Create your views here.
def good_index(request):
    good_list = Good.objects.all() # 把所有 Vendor 的資料取出來
    context = {'good_list': good_list} # 建立 Dict對應到Vendor的資料
    return render(request, 'goods/good_detail.html', context)

def cart_index(request):
    cart_list = Cart.objects.all()
    price_all = Cart.objects.all().aggregate(total=Sum('CartGoodsPrice'))
    return render(request, 'goods/cart.html', {"cart_list":cart_list, 'price_all':price_all})

def cart_add(id):
    good_list = Good.objects.filter(id=id)
    print(good_list)

def manager(request):
    good_list = Good.objects.all()
    cart_list = Cart.objects.all()
    return render(request, 'goods/manager.html', good_list, cart_list)