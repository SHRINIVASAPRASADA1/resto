from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(BestMenu)
class ContentsForBlog(admin.ModelAdmin):
    list_display = ('id', 'Title', 'amount', 'Date','available')


@admin.register(CarouselSlider)
class ContentsForBlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'Title', 'amount', 'Date')

@admin.register(AddToCart)
class AddToCartAdmin(admin.ModelAdmin):
    list_display = ('food_id', 'title', 'date', 'food_id')


@admin.register(BuyNow)
class BuyNowAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'users', 'phonenumber', 'quant')


@admin.register(catogory)
class catogoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

