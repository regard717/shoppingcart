from django.db.models import Sum
from django.shortcuts import render
from .models import Good, Cart, Sold
from goods.form import GoodForm

# Create your views here.
def good_index(request):
    good_list = Good.objects.all() # 把所有 Vendor 的資料取出來
    return render(request, 'goods/good_detail.html', {'good_list': good_list})

def cart_index(request):
    cart_list = Cart.objects.all()
    price_all = Cart.objects.all().aggregate(total=Sum('CartGoodsPrice'))
    discount = int(price_all['total'])//1000
    if discount != 0:
        discount *= 100
        x = int(price_all['total']) - discount
        price_all['total'] = str(x)
        return render(request, 'goods/cart.html', {"cart_list":cart_list, 'price_all':price_all})
    else:
        return render(request, 'goods/cart.html', {"cart_list":cart_list, 'price_all':price_all})

def cart_add(request, vlist_id):
    add_good_to_cart = Good.objects.get(pk=vlist_id)
    if not Cart.objects.filter(CartGoodsName=add_good_to_cart.GoodsName):
        add_good_to_cart.GoodsQuantity='1'
        Cart.objects.create(CartGoodsName=add_good_to_cart.GoodsName, CartGoodsPrice=add_good_to_cart.GoodsPrice, CartGoodsQuantity=add_good_to_cart.GoodsQuantity)
    else :
        quantity = Cart.objects.filter(CartGoodsName=add_good_to_cart.GoodsName)
        for i in quantity:
            x = i.CartGoodsQuantity
            y = i.CartGoodsPrice
        x += 1
        y += add_good_to_cart.GoodsPrice
        Cart.objects.filter(CartGoodsName=add_good_to_cart.GoodsName).update(CartGoodsQuantity=x, CartGoodsPrice=y)
    good_list = Good.objects.all()
    return render(request, 'goods/good_detail.html', {'good_list': good_list})

def check_out(request):
    unsold = Cart.objects.all()
    sold = Sold.objects.all()
    for i in unsold:
        for j in sold:
            if i.CartGoodsName==j.SoldGoodsName :
                j.SoldGoodsPrice += i.CartGoodsPrice
                j.SoldGoodsQuantity += i.CartGoodsQuantity
                Sold.objects.filter(SoldGoodsName=i.CartGoodsName).update(SoldGoodsPrice=j.SoldGoodsPrice, SoldGoodsQuantity=j.SoldGoodsQuantity)
                Cart.objects.filter(CartGoodsName=i.CartGoodsName).delete()
    last_unsold = Cart.objects.all()
    for i in last_unsold:
        Sold.objects.create(SoldGoodsName=i.CartGoodsName, SoldGoodsPrice=i.CartGoodsPrice, SoldGoodsQuantity=i.CartGoodsQuantity)
    Cart.objects.all().delete()
    return render(request, 'goods/check_out.html')

def askdelete(request, clist_CartGoodsName):
    Cart.objects.filter(CartGoodsName=clist_CartGoodsName).delete()
    cart_list = Cart.objects.all()
    price_all = Cart.objects.all().aggregate(total=Sum('CartGoodsPrice'))
    return render(request, 'goods/cart.html', {"cart_list":cart_list, 'price_all':price_all})

def manager(request):
    good_list = Good.objects.all()
    sold_list = Sold.objects.all()
    return render(request, 'goods/manager.html', {'good_list':good_list, 'sold_list':sold_list})

def plusQuantity(request, vlist_GoodsName):
    plusName = Good.objects.filter(GoodsName=vlist_GoodsName)
    for i in plusName :
        x = i.GoodsQuantity
    x += 1
    Good.objects.filter(GoodsName=vlist_GoodsName).update(GoodsQuantity=x)
    good_list = Good.objects.all()
    sold_list = Sold.objects.all()
    return render(request, 'goods/manager.html', {'good_list':good_list, 'sold_list':sold_list})


def minusQuantity(request, vlist_GoodsName):
    plusName = Good.objects.filter(GoodsName=vlist_GoodsName)
    for i in plusName :
        x = i.GoodsQuantity
    x -= 1
    Good.objects.filter(GoodsName=vlist_GoodsName).update(GoodsQuantity=x)
    good_list = Good.objects.all()
    sold_list = Sold.objects.all()
    return render(request, 'goods/manager.html', {'good_list':good_list, 'sold_list':sold_list})


def deleteGoods(request, vlist_GoodsName):
    Good.objects.filter(GoodsName=vlist_GoodsName).delete()
    good_list = Good.objects.all()
    sold_list = Sold.objects.all()
    return render(request, 'goods/manager.html', {'good_list':good_list, 'sold_list':sold_list})

def shipping(request, slist_SoldGoodsName):
    shipName = Good.objects.get(GoodsName=slist_SoldGoodsName)
    quantity = Sold.objects.get(SoldGoodsName=shipName.GoodsName)
    last = shipName.GoodsQuantity - quantity.SoldGoodsQuantity
    Good.objects.filter(GoodsName=slist_SoldGoodsName).update(GoodsQuantity=last)
    Sold.objects.filter(SoldGoodsName=shipName.GoodsName).delete()
    good_list = Good.objects.all()
    sold_list = Sold.objects.all()
    return render(request, 'goods/manager.html', {'good_list':good_list, 'sold_list':sold_list})

def add_function(request):
    if request.method == 'POST':
        GoodsName = request.POST['Goodsname']
        GoodsPrice = request.POST['Goodsprice']
        GoodsQuantity = request.POST['Goodsquantity']
        Good.objects.create(GoodsName=GoodsName, GoodsPrice=GoodsPrice, GoodsQuantity=GoodsQuantity)
    good_list = Good.objects.all()
    sold_list = Sold.objects.all()
    return render(request, 'goods/manager.html', {'good_list':good_list, 'sold_list':sold_list})