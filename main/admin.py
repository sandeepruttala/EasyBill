from django.contrib import admin
from .models import Table, Item, Order, OrderHistory
# Register your models here.
admin.site.register(Table)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderHistory)
