from django import forms
from goods import models
from .models import Good

class GoodForm(forms.Form):
    GoodsName = forms.CharField(max_length = 30, label="商品名稱")
    GoodsPrice = forms.DecimalField(max_digits = 4, decimal_places=0, label="商品價格")
    GoodsQuantity = forms.DecimalField(max_digits = 4, decimal_places=0, label="商品數量")
