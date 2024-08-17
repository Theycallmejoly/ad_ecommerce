from django.db import models
from  django.contrib.auth.models import User





class Category (models.Model):
    title = models.CharField(max_length=80)



# Create your models here.
class Product (models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    price = models.DecimalField(decimal_places=2)
    image = models.ImageField()
    quantity = models.PositiveIntegerField()
    stauts = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)



class Cart (models.Model):
    quantity = models.PositiveIntegerField()
    Product = models.ForeignKey(Product , on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)



class Order (models.Model):
    total_price = models.DecimalField(decimal_places=2)
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    status = models.BooleanField(null=True)



class OrderProduct(models.Model):
    order = models.ForeignKey(Order , on_delete=models.CASCADE)
    Product = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateField(auto_now_add=True)
    price = models.DecimalField(decimal_places=2)


class PeymentLog(models.Model):
    amount = models.DecimalField(decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.PositiveIntegerField()
    order_id = models.PositiveIntegerField()
    status = models.CharField(max_length=90)
    error_code = models.CharField(max_length=300)