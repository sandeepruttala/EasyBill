from django.contrib import admin
from .models import Table, Item, Order, OrderHistory, Category
# Register your models here.
admin.site.register(Table)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderHistory)
admin.site.register(Category)