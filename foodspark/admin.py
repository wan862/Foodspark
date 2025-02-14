from django.contrib import admin
from .models import *

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'address', 'imgurl')

class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('resid', 'name', 'cuisine', 'price' )

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'restaurant', 'foodlist', 'foodqty', 'amount', 'ordertime', 'orderdate', 'status')

class CartAdmin(admin.ModelAdmin):
    list_display = ('customer', 'fooditem', 'foodqty')

# Register your models here.
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(FoodItem, FoodItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Cart, CartAdmin)
