from django.db import models

# Create your models here.

# table
class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    table_name  = models.CharField(max_length=100,default="Table"+str(table_number))
    def __str__(self):
        return self.table_name

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    table_number = models.ForeignKey(Table, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.order_name
    
class OrderHistory(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_name = "Order"+str(order_id)
    table_number = models.ForeignKey(Table, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_name
