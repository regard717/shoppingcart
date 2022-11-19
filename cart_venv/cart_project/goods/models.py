from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Good(models.Model):
    GoodsName = models.CharField(max_length = 30) # 商品的名稱
    GoodsPrice = models.DecimalField(max_digits = 4, decimal_places=0) # 商品價錢
    GoodsQuantity = models.DecimalField(max_digits = 4, decimal_places=0) # 商品數量

    def __str__(self):
        return self.GoodsName

class Cart(models.Model):
    CartGoodsName = models.CharField(max_length = 30) # 購物車裡的商品名稱
    CartGoodsPrice = models.DecimalField(max_digits = 4, decimal_places=0) # 購物車裡的商品價錢
    CartGoodsQuantity = models.DecimalField(max_digits = 4, decimal_places=0) # 購物車裡的商品數量

    def __str__(self):
        return self.CartGoodsName
    
class Sold(models.Model):
    soldGoodsName = models.CharField(max_length = 30) # 購物車裡的商品名稱
    soldGoodsPrice = models.DecimalField(max_digits = 4, decimal_places=0) # 購物車裡的商品價錢
    soldGoodsQuantity = models.DecimalField(max_digits = 4, decimal_places=0) # 購物車裡的商品數量

    def __str__(self):
        return self.soldGoodsName

@admin.register(Good)
class GoodAdmin(admin.ModelAdmin) :
    list_display = [field.name for field in Good._meta.fields]
    search_fields = ('GoodsName', 'GoodsPrice')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin) :
    list_display = [field.name for field in Cart._meta.fields]

@admin.register(Sold)
class SoldAdmin(admin.ModelAdmin) :
    list_display = [field.name for field in Sold._meta.fields]