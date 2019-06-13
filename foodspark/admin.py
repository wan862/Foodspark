from django.contrib import admin

from .models import *

# Register your models here.

#admin.site.register(Customer)
#admin.site.register(Restaurant)
#admin.site.register(FoodItem)
#admin.site.register(Order)
#admin.site.register(Cart)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'address')

class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('resid', 'name', 'cuisine', 'price', 'availability_time')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'restaurant', 'foodlist', 'foodqty', 'amount', 'ordertime', 'orderdate', 'deliverystatus')

class CartAdmin(admin.ModelAdmin):
    list_display = ('customer', 'fooditem', 'foodqty')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(FoodItem, FoodItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Cart, CartAdmin)
