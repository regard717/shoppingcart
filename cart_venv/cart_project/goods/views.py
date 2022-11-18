from django.shortcuts import render
from .models import Good, Cart

# Create your views here.
def good_index(request):
    good_list = Good.objects.all() # 把所有 Vendor 的資料取出來
    context = {'good_list': good_list} # 建立 Dict對應到Vendor的資料
    return render(request, 'goods/good_detail.html', context)

def cart_index(request):
    cart_list = Cart.objects.all()
    context = {'cart_list': cart_list}
    return render(request, 'goods/cart.html', context)

def cart_add(id):
    good_list = Good.objects.filter(id=id)
    print(good_list)

    


