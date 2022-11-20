from django.contrib import admin
from .models import Good, Cart, Sold
from import_export.admin import ImportExportModelAdmin

@admin.register(Good)
class GoodAdmin(ImportExportModelAdmin) :
    list_display = [field.name for field in Good._meta.fields]

@admin.register(Cart)
class CartAdmin(ImportExportModelAdmin) :
    list_display = [field.name for field in Cart._meta.fields]

@admin.register(Sold)
class SoldAdmin(ImportExportModelAdmin) :
    list_display = [field.name for field in Sold._meta.fields]